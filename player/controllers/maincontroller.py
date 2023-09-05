from odoo import http
from .controllers import PlayerController

class ReplacePlayerController(PlayerController):
    # 1 request bình thường
    @http.route('/player')
    def player_check_1(self):
        super(ReplacePlayerController, self).player_check_1()
        return 'Danbmt danbmt danbmt xps xps'
