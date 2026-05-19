from odoo import http
from odoo.http import request


class DateFormAdvancedWidget(http.Controller):
    @http.route(
        "/date_form_advanced",
        type="http",
        auth="public",
        website=True,
        sitemap=True,
    )
    def date_form_advanced(self):
        return request.render("date_form_advanced_widget.date_form_advanced_page")

    @http.route(
        "/gaesteregistrierung",
        type="http",
        auth="public",
        website=True,
        sitemap=True,
    )
    def gaesteregistrierung(self):
        countries = request.env["res.country"].search([], order="name")
        top = countries.filtered(lambda c: c.preferred_guest_registration)
        rest = countries - top
        return request.render(
            "date_form_advanced_widget.gaesteregistrierung_page",
            {"countries_top": top, "countries_rest": list(rest)},
        )
