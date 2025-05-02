from odoo import models,fields,api



class BusRoute(models.Model):
    _name="busroute.model"
    _description="Bus route details of student"


    bus_route_no = fields.Char(string="Bus Route No")
    bus_no = fields.Char(string="Bus No")
    route = fields.Char(string="Route")
    from_location = fields.Char(string="From")
    to = fields.Char(string="To")
    arrival_time = fields.Char(string="Arrival Time")
    driver_name = fields.Char(string="Driver Name")
    driver_phone = fields.Char(string="Driver Number")

