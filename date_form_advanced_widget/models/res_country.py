from odoo import fields, models

_PREFERRED_CODES = ["AT", "DE", "NL", "CZ", "FR", "GB", "CH", "IT", "ES"]


class ResCountry(models.Model):
    _inherit = "res.country"

    preferred_guest_registration = fields.Boolean(
        string="Preferred in Guest Registration",
        default=False,
    )

    def action_set_default_preferred_guest_registration(self):
        self.search([]).write({"preferred_guest_registration": False})
        self.search([("code", "in", _PREFERRED_CODES)]).write(
            {"preferred_guest_registration": True}
        )
