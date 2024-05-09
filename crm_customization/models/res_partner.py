from odoo import models, fields, api


# This class inherits from res.partner, a model for partners/contacts in Odoo.
class Partner(models.Model):
    _inherit = "res.partner"

    # Social network URLs
    # Three fields are defined to store the URLs of the partner’s Facebook, Twitter, and LinkedIn profiles.
    url_facebook = fields.Char('Facebook URL', help='URL of your profile on the social network', copy=False)
    url_twitter = fields.Char('Twitter URL', help='URL of your profile on the social network', copy=False)
    url_linkedin = fields.Char('Linkedin URL', help='URL of your profile on the social network', copy=False)

    # Field to check if the profile is complete
    # A Boolean field that is computed based on the presence of all three social network URLs.
    complete_profile = fields.Boolean('Complete Profile', compute='_compute_complete_profile',
                                      search='_search_complete_profile', default=False)

    # Compute function to set 'complete_profile' to True if all URLs are present
    @api.depends('url_facebook', 'url_twitter', 'url_linkedin')
    def _compute_complete_profile(self):
        for record in self:
            record.complete_profile = all([record.url_facebook, record.url_twitter, record.url_linkedin])

    # Search function to filter records based on the 'complete_profile' status
    def _search_complete_profile(self, operator, value):
        if operator == '=':
            # If searching for records with a complete profile
            records = self.search([('url_facebook', '!=', False), ('url_twitter', '!=', False),
                                   ('url_linkedin', '!=', False)]) if value else self.search(
                ['|', '|', ('url_facebook', '=', False), ('url_twitter', '=', False), ('url_linkedin', '=', False)])
        else:
            # If searching for records without a complete profile
            records = self.search(['|', '|', ('url_facebook', '=', False), ('url_twitter', '=', False),
                                   ('url_linkedin', '=', False)]) if value else self.search(
                [('url_facebook', '!=', False), ('url_twitter', '!=', False), ('url_linkedin', '!=', False)])
        return [('id', 'in', records.ids)]
