# -*- coding: utf-8 -*-

import urllib
from base import BasePaster

class SlexyPaster(BasePaster):

	_host = 'slexy.org'
	_uri = '/index.php/submit'
	_method = 'POST'
	_ssl = False

	def paste(self):
		data = {
	    	'raw_paste': self.prepare(),
	        'comment': '',
	        'author': self.poster(),
	        'language': self.prepare_syntax(),
	        'permissions': 1 if self.private() else 0,
	        'desc': self.description(),
	        'linenumbers': 0,
	        'expire': self.prepare_ttl(),
	        'tabbing': 'true',
	        'tabtype': 'four',
	        'submit': 'Submit Paste'
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
		if resp.status == 302:
			return h.get('location')

		print resp.status, resp.reason
		return False

	def prepare_ttl(self):
		ttl = self.ttl() * 60
		if ttl > 155520000:
			return 0
		else:
			return ttl

	syntaxes = [
		'text',
		'abap',
		'actionscript',
		'actionscript3',
		'ada',
		'apache',
		'applescript',
		'apt_sources',
		'asm',
		'asp',
		'autoit',
		'avisynth',
		'bash',
		'basic4gl',
		'bf',
		'bibtex',
		'blitzbasic',
		'bnf',
		'boo',
		'c',
		'c_mac',
		'caddcl',
		'cadlisp',
		'cfdg',
		'cfm',
		'cil',
		'cmake',
		'cobol',
		'cpp-qt',
		'cpp',
		'csharp',
		'css',
		'd',
		'dcs',
		'delphi',
		'diff',
		'div',
		'dos',
		'dot',
		'eiffel',
		'email',
		'erlang',
		'fo',
		'fortran',
		'freebasic',
		'genero',
		'gettext',
		'glsl',
		'gml',
		'gnuplot',
		'groovy',
		'haskell',
		'hq9plus',
		'html4strict',
		'idl',
		'ini',
		'inno',
		'intercal',
		'io',
		'java',
		'java5',
		'javascript',
		'kixtart',
		'klonec',
		'klonecpp',
		'latex',
		'lisp',
		'locobasic',
		'lolcode',
		'lotusformulas',
		'lotusscript',
		'lscript',
		'lsl2',
		'lua',
		'm68k',
		'make',
		'matlab',
		'mirc',
		'modula3',
		'mpasm',
		'mxml',
		'mysql',
		'nsis',
		'oberon2',
		'objc',
		'ocaml',
		'oobas',
		'oracle11',
		'oracle8',
		'pascal',
		'per',
		'perl',
		'php',
		'pic16',
		'pixelbender',
		'plsql',
		'povray',
		'powershell',
		'progress',
		'prolog',
		'properties',
		'providex',
		'python',
		'qbasic',
		'rails',
		'rebol',
		'reg',
		'robots',
		'ruby',
		'sas',
		'scala',
		'scheme',
		'scilab',
		'sdlbasic',
		'smalltalk',
		'smarty',
		'sql',
		'tcl',
		'teraterm',
		'thinbasic',
		'tsql',
		'typoscript',
		'vb',
		'vbnet',
		'verilog',
		'vhdl',
		'vim',
		'visualfoxpro',
		'visualprolog',
		'whitespace',
		'whois',
		'winbatch',
		'xml',
		'xorg_conf',
		'xpp',
		'z80'
	]
