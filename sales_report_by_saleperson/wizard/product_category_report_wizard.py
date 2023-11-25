from odoo import api, fields, models
import pytz
from pytz import timezone
from datetime import datetime


class ProductcategoryWizard(models.TransientModel):
    _name = 'category.wizard'

    start_date=fields.Datetime('Start Date', default=fields.Datetime.now(), required=True)
    end_date=fields.Datetime(string="End Date", default=fields.Datetime.now(), required=True)
    categ_id = fields.Many2one('product.category', 'Product category', required=False)
    user=fields.Many2many('res.users', string="Bill User",required=False)
    @api.multi
    def sale_productcategory_report(self,data):

        return self.env['report'].get_action(self,'sales_report_by_saleperson.sale_productcate',data=data)