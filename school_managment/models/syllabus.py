from odoo import models,fields,api
from datetime import date


class Syllabus(models.Model):
    _name="syllabus.model"
    _description="view syllabus"

    syllabus_file = fields.Binary(string="Syllabus PDF", required=True, attachment=True)
    std = fields.Selection([('11','11th std'),('12','12th std')])
    department_id = fields.Many2one('department.model',string="Department",ondelete="cascade")
    student_id = fields.Many2one("stulist.model", string="Student")


    def action_download_file(self):
        # Create the attachment if it's not already created
        attachment = self.env['ir.attachment'].create({
            'name': self.file_name or "downloaded_file",
            'type': 'binary',
            'datas': self.syllabus_file,
            'store_fname': self.file_name or "downloaded_file",
            'mimetype': 'application/octet-stream',  # You can modify the MIME type based on the file type
        })

        # Provide the file download URL `
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%d?download=true' % attachment.id,
            'target': 'new',
        }

