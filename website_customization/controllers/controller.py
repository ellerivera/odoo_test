from odoo import http
from odoo.http import request


class Request(http.Controller):
    @http.route(['/list_customers'], type="http", auth="user", website=True)
    def customers_promotions_list(self):
        customers = request.env['res.partner'].search([()])
        values = {
            'list_customers_p': customers
        }

        return http.request.render('website_customization.request_promotion', values)
