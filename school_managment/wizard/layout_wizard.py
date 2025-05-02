from odoo import models, fields, api
# import base64
# import tempfile
# from pdf2image import convert_from_bytes


class LayoutWizard(models.TransientModel):
    _name = 'layout.draft.wizard'
    _description = 'Layout Draft Wizard'

    image_preview = fields.Binary("Report Preview", readonly=True)

    def _render_report_to_image(self, report_name):
        pass
        # layout = self.env['layout.draft'].browse(self.env.context.get('active_id'))
        #
        # # Step 1: Render PDF from QWeb report
        # pdf_data, _ = self.env['ir.actions.report']._render_qweb_pdf(report_name, [layout.id])
        #
        # # Step 2: Convert PDF (bytes) to image using pdf2image
        # images = convert_from_bytes(pdf_data, fmt='png', single_file=True)  # Only first page
        #
        # if images:
        #     with tempfile.NamedTemporaryFile(suffix='.png') as tmp:
        #         images[0].save(tmp.name, 'PNG')
        #         tmp.seek(0)
        #         image_base64 = base64.b64encode(tmp.read())
        #         return image_base64
        return False

    def action_set_style(self):
        self.image_preview = self._render_report_to_image('school_managment.print_style_1')

        return self._reopen_wizard()

    def action_button_2(self):
        self.image_preview = self._render_report_to_image('school_managment.print_style_2')

        return self._reopen_wizard()

    def action_button_3(self):
        self.image_preview = self._render_report_to_image('school_managment.print_style_3')

        return self._reopen_wizard()

    def _reopen_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'layout.draft.wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
            'context': self.env.context,
        }


