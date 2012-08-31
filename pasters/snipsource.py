# -*- coding: utf-8 -*-

import urllib
import re
from base import BasePaster

class SnipsourcePaster(BasePaster):

	_host = 'snipsource.com'
	_uri = '/includes/parser.php'
	_method = 'POST'
	_ssl = False

	def paste(self):
		data = {
	    	'code': self.prepare(),
	        'drop': self.prepare_syntax(id = True),
	        'code_title': self.description(),
	       	'password': '' if not self.password() else self.password(),
	       	'captcha': 'undefined'
		}

		data = urllib.urlencode(data)
		headers = {
			'Content-type': 'application/x-www-form-urlencoded',
			'Accept': 'text/plain'
		}

		(resp, d, h) = self.httpRequest(
				host=self._host,
				uri=self._uri,
				method=self._method,
				ssl=self._ssl,
				data=data,
				headers=headers
			)

		# Success
		r = re.compile(r'http://snipsource\.com/[0-9]+')
		if resp.status == 200 and r.search(d):
			return r.search(d).group(0)

		print resp.status, resp.reason
		return False

	def prepare_syntax(self, syntax = None, id = False, **kwargs):
		s = super(SnipsourcePaster, self).prepare_syntax(syntax = syntax, **kwargs)
		if id:
			return self.syntaxes[s]
		else:
			return s

	def supportedSyntaxes(self):
		return self.syntaxes.keys()

	syntaxes = {
		'txt': '1',
		'js': '2',
		'php': '3',
		'cpp': '5',
		'actionscript': '6',
		'apache': '7',
		'applescript': '8',
		'awk': '9',
		'bash': '10',
		'c': '11',
		'csharp': '12',
		'css': '13',
		'delphi': '14',
		'fortran': '15',
		'haskell': '16',
		'java': '17',
		'jquery': '18',
		'modula2': '19',
		'mysql': '20',
		'perl': '21',
		'python': '22',
		'ror': '23',
		'scheme': '24',
		'sql': '25',
		'vb': '26',
		'vbnet': '27',
		'vim': '28',
		'xml': '29',
		'unknown': '4'
	}
