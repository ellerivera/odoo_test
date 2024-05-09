from odoo import http
from odoo.http import request


class Request(http.Controller):

    # Route to list all customers
    @http.route(['/list_customers'], type="http", auth="user", website=True)
    def customers_promotions_list(self):

        # Retrieves all customer records
        customers = request.env['res.partner'].search([])
        values = {
            'list_customers_p': customers
        }

        # Renders the list on the specified webpage template
        return http.request.render('website_customization.request_customers_promotions', values)

    # Route to view a specific customer's details
    @http.route(['/view_customer'], type="http", auth="user", website=True)
    def request_view_customer(self, **kw):

        # Searches for a customer by ID provided in the URL parameters
        customer = request.env['res.partner'].search([('id', '=', int(kw['parameter']))])

        # Renders the customer's details on the specified webpage template
        return http.request.render('website_customization.view_customers_promotions', {'customer': customer})

    # Route to filter customers based on provided criteria
    @http.route(['/filter'], type="http", auth="user", website=True)
    def search_customers(self, **kwargs):

        # Checks if the filter parameter is present in the URL
        if 'filter' in kwargs:

            # Retrieves filter criteria from URL parameters
            name = kwargs.get('name', '')
            url_facebook = kwargs.get('url_facebook', '')
            url_twitter = kwargs.get('url_twitter', '')
            url_linkedin = kwargs.get('url_linkedin', '')

            # Builds the search domain based on the presence of filter criteria
            domain = []
            if name:
                domain.append(('name', 'ilike', name))
            if url_facebook:
                domain.append(('url_facebook', 'ilike', url_facebook))
            if url_twitter:
                domain.append(('url_twitter', 'ilike', url_twitter))
            if url_linkedin:
                domain.append(('url_linkedin', 'ilike', url_linkedin))

            # Searches for customers matching the domain criteria
            customers = http.request.env['res.partner'].search(domain)
            values = {
                'list_customers_p': customers
            }

            # Renders the filtered list on the specified webpage template
            return http.request.render('website_customization.request_customers_promotions', values)
        else:

            # If no filter is applied, retrieves all customers
            customers = request.env['res.partner'].search([])
            values = {
                'list_customers_p': customers
            }

            # Renders the unfiltered list on the specified webpage template
            return http.request.render('website_customization.request_customers_promotions', values)
