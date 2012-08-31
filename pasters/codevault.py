# -*- coding: utf-8 -*-

import urllib
from base import BasePaster

class CodevaultPaster(BasePaster):

	_host = 'vault.somecode.me'
	_uri = '/'
	_method = 'POST'
	_ssl = False
	_defaultSyntax = 'no-highlight'

	def paste(self):
		data = {
			'code_data': self.prepare(),
			'language_list': self.prepare_syntax()
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
			return 'http://' + self._host + h.get('location', False)

		print resp.status, resp.reason
		return False

	syntaxes = [
		'no-highlight',
		'1c',
		'actionscript',
		'apache',
		'avrasm',
		'axapta',
		'bash',
		'cmake',
		'coffeescript',
		'cpp',
		'cs',
		'css',
		'd',
		'delphi',
		'diff',
		'xml',
		'django',
		'dos',
		'erlang-repl',
		'erlang',
		'glsl',
		'go',
		'haskell',
		'http',
		'ini',
		'java',
		'javascript',
		'json',
		'lisp',
		'lua',
		'markdown',
		'matlab',
		'mel',
		'nginx',
		'objectivec',
		'parser3',
		'perl',
		'php',
		'profile',
		'python',
		'r',
		'rib',
		'rsl',
		'ruby',
		'rust',
		'scala',
		'smalltalk',
		'sql',
		'tex',
		'vala',
		'vbscript',
		'vhdl'
	]
