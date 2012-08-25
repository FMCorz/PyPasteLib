# -*- coding: utf-8 -*-

import urllib
from base import BasePaster

class UbuntuPaster(BasePaster):

	_host = 'paste.ubuntu.com'
	_uri = '/'
	_method = 'POST'
	_ssl = False

	def paste(self):
		data = {
			'poster': self.poster(),
			'syntax': self.prepare_syntax(keepWhenMissing = False),
			'content': self.prepare()
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
			return h.get('location', False)

		print resp.status, resp.reason
		return False

	syntaxes = [
		'apacheconf',
		'as',
		'bash',
		'bat',
		'bbcode',
		'befunge',
		'boo',
		'c',
		'c-objdump',
		'common-lisp',
		'control',
		'cpp',
		'cpp-objdump',
		'csharp',
		'css',
		'css+django',
		'css+erb',
		'css+genshitext',
		'css+mako',
		'css+myghty',
		'css+php',
		'css+smarty',
		'd',
		'd-objdump',
		'delphi',
		'diff',
		'django',
		'dylan',
		'erb',
		'erlang',
		'gas',
		'genshi',
		'genshitext',
		'groff',
		'haskell',
		'html',
		'html+django',
		'html+genshi',
		'html+mako',
		'html+myghty',
		'html+php',
		'html+smarty',
		'ini',
		'irc',
		'java',
		'js',
		'js+django',
		'js+erb',
		'js+genshitext',
		'js+mako',
		'js+myghty',
		'js+php',
		'js+smarty',
		'jsp',
		'lhs',
		'llvm',
		'lua',
		'make',
		'mako',
		'minid',
		'moocode',
		'mupad',
		'myghty',
		'mysql',
		'objdump',
		'objective-c',
		'ocaml',
		'perl',
		'php',
		'pot',
		'pycon',
		'pytb',
		'python',
		'raw',
		'rb',
		'rbcon',
		'redcode',
		'rhtml',
		'rst',
		'scheme',
		'smarty',
		'sourceslist',
		'sql',
		'squidconf',
		'tex',
		'text',
		'trac-wiki',
		'vb.net',
		'vim',
		'xml',
		'xml+django',
		'xml+erb',
		'xml+mako',
		'xml+myghty',
		'xml+php',
		'xml+smarty'
	]
