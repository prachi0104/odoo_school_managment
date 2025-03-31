from odoo import models,fields,api,_
from odoo.exceptions import ValidationError
from datetime import timedelta
from datetime import date

class CronModel(models.Model):
    _name='cron'


    @api.model
    def test_cron_job(self):
        print("test_cron_created")



