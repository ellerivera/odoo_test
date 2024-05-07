from odoo import models, fields, api, _


class Partner(models.Model):
    _inherit = "res.partner"

    url_facebook = fields.Char('Facebook URL', help='URL of your profile on the social network', copy=False)
    url_twitter = fields.Char('Twitter URL', help='URL of your profile on the social network', copy=False)
    url_linkedin = fields.Char('Linkedin URL', help='URL of your profile on the social network', copy=False)

    complete_profile = fields.Boolean('Complete Profile', compute='_compute_complete_profile', default=False)

    @api.depends('url_facebook', 'url_twitter', 'url_linkedin')
    def _compute_complete_profile(self):
        for record in self:
            if record.url_facebook and record.url_twitter and record.url_linkedin:
                record.complete_profile = True
