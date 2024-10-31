
# models/hospital_bed.py
class HospitalBed(models.Model):
    _name = 'hospital.bed'
    _description = 'Hospital Bed'

    name = fields.Char(string='Bed Number', required=True)
    room_id = fields.Many2one('hospital.room', string='Room', required=True)
    is_occupied = fields.Boolean(string='Occupied', default=False)
    current_patient_id = fields.Many2one('medical.patient', string='Current Patient')