from odoo import http
from odoo.http import request


class Request(http.Controller):
    @http.route(['/list_customers'], type="http", auth="user", website=True)
    def customers_promotions_list(self):
        customers = request.env['res.partner'].search([])
        values = {
            'list_customers_p': customers
        }

        return http.request.render('website_customization.request_customers_promotions', values)

    @http.route(['/view_customer'], type="http", auth="user", website=True)
    def request_view_customer(self, **kw):
        customer = request.env['res.partner'].search([('id', '=', int(kw['parameter']))])

        return http.request.render('website_customization.view_customers_promotions', {'customer': customer})

    @http.route(['/filter'], type="http", auth="user", website=True)
    def search_customers(self, **kwargs):
        if 'filter' in kwargs:
            name = kwargs.get('name', '')
            url_facebook = kwargs.get('url_facebook', '')
            url_twitter = kwargs.get('url_twitter', '')
            url_linkedin = kwargs.get('url_linkedin', '')

            domain = []
            if name:
                domain.append(('name', 'ilike', name))
            if url_facebook:
                domain.append(('url_facebook', 'ilike', url_facebook))
            if url_twitter:
                domain.append(('url_twitter', 'ilike', url_twitter))
            if url_linkedin:
                domain.append(('url_linkedin', 'ilike', url_linkedin))

            customers = http.request.env['res.partner'].search(domain)
            values = {
                'list_customers_p': customers
            }
            return http.request.render('website_customization.request_customers_promotions', values)
        else:
            customers = request.env['res.partner'].search([])
            values = {
                'list_customers_p': customers
            }

            return http.request.render('website_customization.request_customers_promotions', values)
