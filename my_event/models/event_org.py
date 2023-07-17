from odoo import models, fields

class event_org(models.Model):
    _name = "event.org"
    _description = "Event Model"

    name = fields.Char("Event Name")
    date=fields.Date("Date")
    budget = fields.Float("Your Budget")
    venue= fields.Char("Venue")
    # custmer=fields.Many2one('res.partner', string="Custmoer")
    attendees=fields.Integer("Number of Attendees")


