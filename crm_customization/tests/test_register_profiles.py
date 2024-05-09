from odoo.tests.common import TransactionCase


class TestSocialNetworks(TransactionCase):
    def setUp(self):
        super(TestSocialNetworks, self).setUp()
        self.customer = self.env['res.partner'].create({'name': 'Test customer'})

    def test_register_profiles_networks(self):
        self.customer.write({
            'url_facebook': 'https://www.facebook.com/customer',
            'url_twitter': 'https://www.twitter.com/customer',
            'url_linkedin': 'https://www.linkedin.com/customer',
        })

        self.assertEqual(self.customer.url_facebook, 'https://www.facebook.com/customer')
        self.assertEqual(self.customer.url_twitter, 'https://www.twitter.com/customer')
        self.assertEqual(self.customer.url_linkedin, 'https://www.linkedin.com/customer')
