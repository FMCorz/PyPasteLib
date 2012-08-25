# -*- coding: utf-8 -*-

from base import BasePaster

class RawPaster(BasePaster):

	syntaxes = {}

	def paste(self):
		return self.prepare()

	def prepare(self):
		content = ''
		for t in self.texts():
			if t.get('identifier'):
				content += '## ' + str(t.get('identifier'))
				if t.get('syntax', False):
					content += ' [%s]' % self.prepare_syntax(t.get('syntax'))
				content += '\n'
			i = 0
			for text in t.get('text').split('\n'):
				i += 1
				content += '%d: %s\n' % (i, text)
			content += '\n'
		return content.strip()
