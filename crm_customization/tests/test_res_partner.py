import unittest

from odoo.tests.common import TransactionCase


class TestPartner(TransactionCase):

    def setUp(self):
        super(TestPartner, self).setUp()

        # Create complete profile
        self.partner_complete = self.env['res.partner'].create({
            'name': 'Complete Customer',
            'email': 'complete@example.com',
            'url_facebook': 'http://facebook.com/complete.customer',
            'url_twitter': 'http://twitter.com/complete.customer',
            'url_linkedin': 'http://linkedin.com/complete.customer'
        })

        # Create complete profile
        self.partner_incomplete = self.env['res.partner'].create({
            'name': 'Incomplete Customer',
            'email': 'incomplete@example.com'

            # Without social networks
        })

    def test_complete_profile(self):
        # Verify that the complete profile has complete_profile set to True
        self.assertTrue(self.partner_complete.complete_profile, "The profile should be complete")

    def test_incomplete_profile(self):
        # Verify that the incomplete profile has complete_profile set to False
        self.assertFalse(self.partner_incomplete.complete_profile, "The profile should not be complete")

    def test_search_complete_profile_true(self):
        # Search complete profile
        complete_profiles = self.env['res.partner']._search_complete_profile('=', True)

        # Verify that only records with a complete profile are returned
        self.assertIn(self.partner_complete.id, [id[1] for id in complete_profiles],
                      "The full profile should be in the results ")
        self.assertNotIn(self.partner_incomplete.id, [id[1] for id in complete_profiles],
                         "The incomplete profile should not be in the results")

    def test_search_complete_profile_false(self):
        # Search incomplete profile
        incomplete_profiles = self.env['res.partner']._search_complete_profile('=', False)

        # Verify that only records with an incomplete profile are returned
        self.assertIn(self.partner_incomplete.id, [id[1] for id in incomplete_profiles],
                      "The incomplete profile should be in the results ")
        self.assertNotIn(self.partner_complete.id, [id[1] for id in incomplete_profiles],
                         "The full profile should not be in the results")


if __name__ == '__main__':
    unittest.main()
