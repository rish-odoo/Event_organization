from odoo import models, fields
from odoo.exceptions import UserError


class event_org(models.Model):
    _name = "event.org"
    _description = "Make your Event"

    name = fields.Char("Event name")
    custmer=fields.Char("Custmer Name")
    cu_m_no=fields.Integer("Custmer Mobile Number")
    cu_m_email=fields.Char("custmer Email")
    description = fields.Text("Description")
    budget = fields.Float("Your Budget")
    venue = fields.Selection([('G', 'Garden'), ('H', 'Hall'),
                             ('Hotel', 'Hotel'), ('re', 'Resturent'), ('cafe', 'Cafe')])
    other_venue=fields.Many2one("event.venue",string="other Venue")
    attendees = fields.Integer("Number of Maximum Attendee")
    active = fields.Boolean('Active', default=True)
    state = fields.Selection(
        [('Co', 'Confirm'), ('C', 'Cancle'), ('N', 'New')])
    date_from=fields.Date("Date from")
    date_to=fields.Date("Date to")

    event_type_id = fields.Many2one("event.type", string="Event-Type")

    service_ids=fields.One2many('event.services','ser_id')

# Have you already booked a vene for the event?



    _sql_constraints = [
        ('check_budget', 'CHECK (budget > 5000)', 'Bugget should be Greater Than 5000')]

    def action_confirm(self):
        # for i in self:
        if self.state == 'Co':
            self.state = "Co"
        else:
            self.state="C"

    def action_cancel(self):
        # for i in self:
        if self.state == 'C':
            self.state = "C"
        else :
            self.state="Co"
