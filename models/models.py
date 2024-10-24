# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class Patient(models.Model):
    _name = 'medical.patient'
    _description = 'Patient Records'

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
