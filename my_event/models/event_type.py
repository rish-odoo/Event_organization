from odoo import models, fields


class event_type(models.Model):
    _name = "event.type"
    _description = "Event Type"
    _order = "name"

    name = fields.Char("Event Name")
    Start_date = fields.Date("Date")
    # end_date = fields.Date("Date")
    budget = fields.Float("Your Budget")
    venue = fields.Char("Venue")
    no_of_guest = fields.Integer("Number of Guest")
    extra_activity = fields.Char("Extra Activities !")
