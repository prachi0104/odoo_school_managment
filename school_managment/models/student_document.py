from odoo import models, fields
from odoo.exceptions import UserError
import logging
import cProfile



class StudentDocument(models.Model):
    _name = 'student.document'
    _description = 'Student Document Upload'

    name = fields.Char("Document Name", required=True)
    student_id = fields.Many2one('stulist.model', string="Student", required=True)
    upload_date = fields.Date("Upload Date", default=fields.Date.today)
    file = fields.Binary("Document File", required=True)
    file_name = fields.Char("Filename")
    description = fields.Text("Description")

    _logger = logging.getLogger(__name__)

    _logger.debug("------------IT IS DEBUG-----------")
    _logger.info("-------------IT IS INFO------------")
    _logger.error("------------IT IS Error-----------")
    _logger.warning("----------IT IS warning---------")
    _logger.critical("----------IT IS Critical---------")

    def action_download_file(self):
        # Create the attachment if it's not already created
        attachment = self.env['ir.attachment'].create({
            'name': self.file_name or "downloaded_file",
            'type': 'binary',
            'datas': self.file,
            'store_fname': self.file_name or "downloaded_file",
            'mimetype': 'application/octet-stream',  # You can modify the MIME type based on the file type
        })

        # Provide the file download URL `
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%d?download=true' % attachment.id,
            'target': 'new',
        }


