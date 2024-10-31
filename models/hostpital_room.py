# models/hospital_room.py
from odoo import models, fields, api

class HospitalRoom(models.Model):
    _name = 'hospital.room'
    _description = 'Hospital Room'

    name = fields.Char(string='Room Number', required=True)
    floor = fields.Char(string='Floor')
    room_type = fields.Selection([
        ('normal', 'Normal'),
        ('icu', 'ICU'),
        ('vip', 'VIP')
    ], string='Room Type', default='normal')
    bed_ids = fields.One2many('hospital.bed', 'room_id', string='Beds')
