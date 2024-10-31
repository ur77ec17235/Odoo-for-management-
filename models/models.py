# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    unsplash_access_key = fields.Char(string='Unsplash Access Key')

class Patient(models.Model):
    _name = 'medical.patient'
    _description = 'Patient Records'
    _inherit = 'medical.patient'

    name = fields.Char(string='Patient Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    blood_group = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
    ], string='Blood Group')
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    medical_history = fields.One2many('medical.history', 'patient_id', string='Medical History')
    
    admission_ids = fields.One2many('patient.admission', 'patient_id', string='Admissions')
    current_admission_id = fields.Many2one('patient.admission', string='Current Admission',compute='_compute_current_admission')
    
    @api.depends('admission_ids')
    def _compute_current_admission(self):
        for patient in self:
            current = patient.admission_ids.filtered(
                lambda r: r.state == 'admitted'
            )
            patient.current_admission_id = current and current[0] or False

class MedicalHistory(models.Model):
    _name = 'medical.history'
    _description = 'Medical History Records'

    patient_id = fields.Many2one('medical.patient', string='Patient', required=True)
    date = fields.Date(string='Visit Date', default=fields.Date.today)
    doctor_id = fields.Many2one('medical.doctor', string='Doctor')
    diagnosis = fields.Text(string='Diagnosis')
    prescription = fields.Text(string='Prescription')
    notes = fields.Text(string='Notes')

class Doctor(models.Model):
    _name = 'medical.doctor'
    _description = 'Doctor Records'

    name = fields.Char(string='Doctor Name', required=True)
    specialization = fields.Char(string='Specialization')
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
