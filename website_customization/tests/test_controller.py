from odoo.tests import HttpCase, tagged


@tagged('-at_install', 'post_install')
class TestWebsiteExtension(HttpCase):

    def test_list_customers(self):
        # Test the route to list all customers
        response = self.url_open('/list_customers')
        self.assertEqual(response.status_code, 200, "The route /list_customers should be accessible")

    def test_view_customer(self):
        # Test the route to view a specific customer's details
        response = self.url_open('/view_customer?parameter=1')
        self.assertEqual(response.status_code, 200, "The route /view_customer should be accessible")

    def test_search_customers(self):
        # Test the route to filter customers with POST method
        data = {
            'name': 'Cliente',
            'url_facebook': 'facebook.com/cliente'
        }
        response = self.url_open('/filter', data=data)
        self.assertEqual(response.status_code, 200,
                         "The route /filter should be accessible and return result with method POST")


if __name__ == '__main__':
    HttpCase.main()
