from odoo import models,fields



class CreatePtaWiz(models.TransientModel):
    _name="create.pta.wizard"
    _description="create pta wizard"

    name=fields.Char("Name",required=True)
    enrollment_number=fields.Char("Enrollment Number")
    

    






    

   
