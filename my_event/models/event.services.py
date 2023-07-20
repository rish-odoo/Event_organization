from odoo import api, fields, models


class event_services(models.Model):
    _name = "event.services"
    _description = 'Event services'

    catering = fields.Selection(
        selection=[("Y", "yes"), ("N", "No"),], string="Services", copy=False)

    partner_id = fields.Many2one(
        "res.partner", string="partner", required=True)
    event_id = fields.One2many("event.org", string="Event", required=True)
