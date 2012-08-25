# -*- coding: utf-8 -*-

import urllib
from base import BasePaster

class Paste2Paster(BasePaster):

	_host = 'paste2.org'
	_uri = '/'
	_method = 'POST'
	_ssl = False

	def paste(self):
		data = {
			'description': self.description(),
			'lang': self.prepare_syntax(keepWhenMissing = False),
			'code': self.prepare(),
			'parent': '0'
		}
		data = urllib.urlencode(data)
		headers = { 'Content-type': 'application/x-www-form-urlencoded' }
		(resp, d, h) = self.httpRequest(
				host=self._host,
				uri=self._uri,
				method=self._method,
				ssl=self._ssl,
				data=data,
				headers=headers
			)
		if resp.status == 302:
			return 'http://%s%s' % (self._host, h.get('location', False))

		print resp.status, resp.reason
		return False

	syntaxes = [
		'text',
		'php',
		'mysql',
		'javascript',
		'python',
		'ruby',
		'actionscript',
		'ada',
		'apache',
		'applescript',
		'asm',
		'asp',
		'bash',
		'c',
		'cfm',
		'cpp',
		'csharp',
		'css',
		'd',
		'delphi',
		'diff',
		'eiffel',
		'fortran',
		'html4strict',
		'ini',
		'java',
		'java5',
		'latex',
		'lisp',
		'lua',
		'matlab',
		'perl',
		'qbasic',
		'robots',
		'sql',
		'tcl',
		'vb',
		'vbnet',
		'winbatch',
		'xml',
	]
