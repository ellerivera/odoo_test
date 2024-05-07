from odoo import models, fields, api, _


class Partner(models.Model):
    _inherit = "res.partner"

    url_facebook = fields.Char('Facebook URL', help='URL of your profile on the social network', copy=False)
    url_twitter = fields.Char('Twitter URL', help='URL of your profile on the social network', copy=False)
    url_linkedin = fields.Char('Linkedin URL', help='URL of your profile on the social network', copy=False)
