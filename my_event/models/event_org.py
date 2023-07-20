from odoo import models, fields

class event_org(models.Model):
    _name = "event.org"
    _description = "Make your Event"

    name = fields.Char("Event Name")
    date=fields.Date("Date")
    budget = fields.Float("Your Budget")
    venue= fields.Selection([('G','Garden'),('H','Hall'),('Hotel','Hotel'),('re','Resturent'),('cafe','Cafe')])
    attendees=fields.Integer("Number of Attendees")
    event_type_id=fields.Many2one("event.type",string="Event-Type")
    # service_id=fields.One2many('event.services', 'event_id')
