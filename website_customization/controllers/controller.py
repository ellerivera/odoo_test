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
