# Install Odoo 15

## Bước 1: Cập nhật hệ thống
```
sudo apt update -y && apt upgrade -y
```
## Bước 2: Cài đặt python3 và các thành phần cần thiết
cài đặt thêm `python3` và các `thành phần cần thiết` khác
```
sudo apt install python3-pip  wget python3-dev python3-venv python3-wheel libxml2-dev libpq-dev libjpeg8-dev liblcms2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential git libssl-dev libffi-dev libmysqlclient-dev libjpeg-dev libblas-dev libatlas-base-dev -y
```

## Bước 3: Cài đặt và cấu hình PostgreSQL
```
sudo apt install postgresql -y
```
Sau khi cài đặt thành công `PostgreSQL`, các bạn cần tạo user `PostgreSQL` mới và đặt tên cho user đó là odoo15 với lệnh bên dưới:

```
sudo su - postgres -c "createuser -s odoo15"
```

## Bước 4: Tạo user hệ thống
```
sudo useradd -m -d /opt/odoo15 -U -r -s /bin/bash odoo15
```

## Bước 5: Cài đặt wkhtmltopdf

`Wkhtmltopdf` là một công cụ dòng lệnh mã nguồn mở giúp hiển thị HTML sang định dạng PDF bằng công cụ kết xuất Qt WebKit. Công cụ này cần thiết để `in báo cáo PDF trong Odoo`. Và để cài đặt wkhtmltopdf, các bạn chạy lệnh bên dưới
```
sudo apt-get install wkhtmltopdf -y
```

```
wkhtmltopdf --version
```

## Bước 6: Cài đặt và cấu hình Odoo 15
- Trước khi đi vào cài đặt, đầu tiên các bạn cần truy cập vào user odoo15 đã tạo (Ở bước 3) theo lệnh:
```
su - odoo15
```
** lệnh này sẽ truy cập vào postgresql bằng user odoo15 nhưng sẽ yêu cầu password
** lệnh đúng sẽ là
```
sudo su - odoo15
```

- Tải xuống kho lưu trữ (đặt vào `thư mục /opt/`) Odoo15 từ Github theo lệnh:
```
git clone https://www.github.com/odoo/odoo --depth 1 --branch 15.0 /opt/odoo15/odoo
```

- Di chuyển vào thư mục odoo15 theo lệnh:
```
cd /opt/odoo15
```

- Tạo môi trường ảo theo lệnh:
```
python3 -m venv myodoo15-venv
```

- Kích hoạt môi trường ảo theo lệnh:
```
source myodoo15-venv/bin/activate
```

- Bên trong `môi trường ảo`, bạn `cài đặt các module python cần thiết` theo lệnh:
```
pip3 install wheel
```
```
pip3 install -r odoo/requirements.txt
```

- Thoát môi trường ảo ra theo lệnh:
```
deactivate
```

- Tạo thư mục chứa các module theo lệnh:
```
mkdir /opt/odoo15/custom-addons
```

- Tiến hành thoát khỏi user odoo15 theo lệnh:
```
exit
```

- Tạo `file cấu hình cho Odoo15` theo lệnh:
```
sudo nano /etc/odoo15.conf
```
và thêm `nội dung bên dưới` vào:
```
[options]
; This is the password that allows database operations:
admin_passwd = admin_password
db_host = False
db_port = False
db_user = odoo15
db_password = False
xmlrpc_port = 8069
logfile = /var/log/odoo15/odoo.log
addons_path = /opt/odoo15/odoo/addons,/opt/odoo15/custom-addons
```
trong đó lưu ý file addons_path: là phần viết thêm


- Tạo thư mục ghi log và phân quyền thư mục:

```
mkdir /var/log/odoo15
```
```
chown odoo15:root /var/log/odoo15
```

## Bước 7: Tạo dịch vụ Systemd trên Odoo15
- Để dễ dàng quản lý Odoo15, các bạn cần tạo một file `systemd` theo lệnh:
```
sudo nano /etc/systemd/system/odoo15.service
```

- - Thêm `nội dung` sau vào:
```
[Unit]
Description=Odoo15
Requires=postgresql.service
After=network.target postgresql.service

[Service]
Type=simple
SyslogIdentifier=odoo15
PermissionsStartOnly=true
User=odoo15
Group=odoo15
ExecStart=/opt/odoo15/myodoo15-venv/bin/python3 /opt/odoo15/odoo/odoo-bin -c /etc/odoo15.conf
StandardOutput=journal+console

[Install]
WantedBy=multi-user.target
```

- Tải lại daemon systemd để áp dụng các thay đổi với lệnh:
```
sudo systemctl daemon-reload
```

- Khởi động và kích hoạt dịch vụ Odoo15
```
sudo systemctl enable --now odoo15
```

- Kiểm tra trạng thái của dịch vụ Odoo15.
```
sudo systemctl status odoo15
```

## Bước 8: Truy cập Odoo15 kiểm tra
Sau khi hoàn tất cài đặt, các bạn có thể truy cập Odoo15 theo đường dẫn:
```
http://ipaddress:8069
```