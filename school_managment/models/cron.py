from odoo import models,fields,api,_
from odoo.exceptions import ValidationError
from datetime import timedelta
from datetime import date

class CronModel(models.Model):
    _name='cron'

#written code in hostel_admission.py file
    @api.model
    def test_cron_job(self):
        print("test_cron_created")



