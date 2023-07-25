from odoo import api, fields, models


class event_services(models.Model):
    _name = "event.services"
    _description = 'Event services'

    services= fields.Selection([('Cat','Catering'), ('dec', 'Decoration'), (
        'ph', 'Photography'), ('artist', 'Artist'), ('M', 'Music')], 'Services')
    status=fields.Selection([('Co','Confirm'),('C','Cancle')])
    ammount=fields.Float("Amount")
    total=fields.Float('Sub Total')
    ser_id=fields.Many2one("event.org")  
    vender = fields.Many2one("res.partner", string="vender")
    menue = fields.Char("Make list of Menue")
    seating=fields.Selection([('b',"buffet"),('s',"sit-down"),('d',"dining")],string="seating arrangment",default="b")
    staff_service=fields.Boolean("Do you need staffing services?")
    staff_member=fields.Integer("How many Staff needed",default=10)
   
    def action_accept(self):
        for i in self:
            i.status == "Co"
            i.status = "Confirm"

    def action_refuse(self):
        for i in self:
            i.status == "c"  
            i.status="Cancle" 

