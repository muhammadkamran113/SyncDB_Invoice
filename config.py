# -*- coding: utf-8 -*-

from openerp import models, fields, api

class InvoiceConfigDB(models.TransientModel):
	_inherit = 'base.config.settings'
	_name = 'invoice.config.db'

	user = fields.Char()
	password = fields.Char()
	url = fields.Char()
	db = fields.Char()

	@api.multi
	def set_db_user(self):
		user = self[0].user or ''
		self.env['ir.config_parameter'].set_param('user', user)

	@api.multi
	def set_db_password(self):
		password = self[0].password or ''
		self.env['ir.config_parameter'].set_param('password', password)

	@api.multi
	def set_db_url(self):
		url = self[0].url or ''
		self.env['ir.config_parameter'].set_param('url', url)

	@api.multi
	def set_db_name(self):
		db = self[0].db or ''
		self.env['ir.config_parameter'].set_param('db', db)

	@api.multi
	def get_default_credentials(self, fields=None):
		get_param = self.env['ir.config_parameter'].get_param
		user = get_param('user', default='')
		password = get_param('password', default='')
		url = get_param('url', default='')
		db = get_param('db', default='')
		return {
			'user': user,
			'password': password,
			'url' : url,
			'db' : db
		}