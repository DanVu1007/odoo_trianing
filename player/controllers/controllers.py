# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import random
from datetime import datetime

import json
import werkzeug

class PlayerController(http.Controller):

    # 1 request bình thường
    @http.route('/player', auth="public", type="http")
    def player_check_1(self):
        return 'Danbmt danbmt danbmt'

    # 1 request có params
    @http.route('/player/<int:id>', auth="public", type="http")
    def player_check_2(self, id):
        return 'Danbmt danbmt danbmt %s' % str(id)
    
    # 1 request redirect
    @http.route('/player/redirect', auth="public", type="http")
    def player_check_3(self):
        return werkzeug.utils.redirect('https://viblo.asia/p/two-factor-authentication-with-laravel-5-jvElaO9xKkw')
    
    # 1 request render đến template
    @http.route('/player/login', auth="public", type="http")
    def player_check_4(self):
        return request.render("web.login")
    
    # 1 request trả về 1 json
    @http.route('/player/json', auth="public", type="http")
    def player_check_5(self):
        return json.dumps({
            'check': 'danbmt'
        })
    
    # 1 request tạo một player mới
    @http.route('/player/newplayer', auth="public", type="http")
    def player_check_6(self):
        name_list = ['Kiều Phong', 'Hư Trúc', 'Mộ Dung Phục', 'Quách Tĩnh', 'Hoàng Dung']

        player =  request.env['player'].sudo().create({
            'name': random.choice(name_list),
            'country': 'Liêu',
            'gender': 'male',
            'position': 'Cái bang %s' % (datetime.now().time()),
            'height': 180,
            'weight': 100
        })
        return request.redirect(request.httprequest.referrer or '/')
    