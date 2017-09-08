# -*- coding: utf-8 -*-

import xmlrpclib

from openerp import models, fields, api
from openerp.exceptions import ValidationError

class create_invoice_db(models.Model):
	_inherit = 'account.invoice'

	@api.multi
	def create_db_invoice(self):
		get_param = self.env['ir.config_parameter'].get_param
		username = get_param('user', default='')
		password = get_param('password', default='')
		url = get_param('url', default='')
		db = get_param('db', default='')
		if username and password and url and db:
			print username
			print password
			print url
			print db
			common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
			uid = common.authenticate(db, username, password, {})
			models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
			new_invoice = models.execute_kw(db, uid, password, 'account.invoice', 'create', [{
				'partner_id': self.partner_id.id,
				'journal_id': self.journal_id.id,
				'account_id': self.account_id.id,
				# 'invoice_line': self.invoice_line.id,
			}])
		else:
			raise ValidationError("Please configure db credential in setting...!")