from odoo import models, fields


class event_type(models.Model):
    
    _name = "event.type"
    _description = "Event Type"
    _order = "name"

    name = fields.Char("Event Name")
    Start_date = fields.Date("Date")
    end_date = fields.Date("Date")
    budget = fields.Float("Your Budget")
    venue= fields.Selection([('G','Garden'),('H','Hall'),('Hotel','Hotel'),('re','Resturent'),('cafe','Cafe')])
    no_of_guest = fields.Integer("Number of Guest")
    # event_ids=fields.One2many("event.org","event_type_id",String="Event Type")  
      
