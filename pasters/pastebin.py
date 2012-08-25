# -*- coding: utf-8 -*-

import urllib
from base import BasePaster

class PastebinPaster(BasePaster):

	apikey = None

	_api = 'pastebin.com'
	_uri = '/api/api_post.php'
	_method = 'POST'
	_ssl = False

	def __init__(self, **kwargs):
		BasePaster.__init__(self, **kwargs)
		if not self.setting('apikey'):
			raise Exception('An API key is required')

	def paste(self):
		data = {
			'api_option': 'paste',
			'api_dev_key': self.setting('apikey'),
			'api_paste_code': self.prepare(),
			'api_paste_name': self.description(),
			'api_paste_private': self.prepare_private(),
			'api_paste_expire_date': self.prepare_ttl()
		}

		syntax = self.prepare_syntax()
		if syntax:
			data['api_paste_format'] = syntax

		data = urllib.urlencode(data)
		headers = { "Content-type": "application/x-www-form-urlencoded" }
		(resp, d, h) = self.httpRequest(
				host=self._api,
				uri=self._uri,
				method=self._method,
				ssl=self._ssl,
				data=data,
				headers=headers
			)

		if resp.status == 200:
			return d
		else:
			print resp.status, resp.reason
			return False

	def prepare_private(self):
		return 2 if self.private() else 0

	def prepare_ttl(self):
		ttl = self.ttl()
		if ttl == None:
			return 'N'
		elif ttl <= 10:
			return '10M'
		elif ttl <= 60:
			return '1H'
		elif ttl <= 60 * 24:
			return '1D'
		else:
			return '1M'

	syntaxes = [
	   	'4cs',
	    '6502acme',
	    '6502kickass',
	    '6502tasm',
	    'abap',
	    'actionscript',
	    'actionscript3',
	    'ada',
	    'algol68',
	    'apache',
	    'applescript',
	    'apt_sources',
	    'asm',
	    'asp',
	    'autoconf',
	    'autohotkey',
	    'autoit',
	    'avisynth',
	    'awk',
	    'bascomavr',
	    'bash',
	    'basic4gl',
	    'bibtex',
	    'blitzbasic',
	    'bnf',
	    'boo',
	    'bf',
	    'c',
	    'c_mac',
	    'cil',
	    'csharp',
	    'cpp',
	    'cpp-qt',
	    'c_loadrunner',
	    'caddcl',
	    'cadlisp',
	    'cfdg',
	    'chaiscript',
	    'clojure',
	    'klonec',
	    'klonecpp',
	    'cmake',
	    'cobol',
	    'coffeescript',
	    'cfm',
	    'css',
	    'cuesheet',
	    'd',
	    'dcs',
	    'delphi',
	    'oxygene',
	    'diff',
	    'div',
	    'dos',
	    'dot',
	    'e',
	    'ecmascript',
	    'eiffel',
	    'email',
	    'epc',
	    'erlang',
	    'fsharp',
	    'falcon',
	    'fo',
	    'f1',
	    'fortran',
	    'freebasic',
	    'freeswitch',
	    'gambas',
	    'gml',
	    'gdb',
	    'genero',
	    'genie',
	    'gettext',
	    'go',
	    'groovy',
	    'gwbasic',
	    'haskell',
	    'hicest',
	    'hq9plus',
	    'html4strict',
	    'html5',
	    'icon',
	    'idl',
	    'ini',
	    'inno',
	    'intercal',
	    'io',
	    'j',
	    'java',
	    'java5',
	    'javascript',
	    'jquery',
	    'kixtart',
	    'latex',
	    'lb',
	    'lsl2',
	    'lisp',
	    'llvm',
	    'locobasic',
	    'logtalk',
	    'lolcode',
	    'lotusformulas',
	    'lotusscript',
	    'lscript',
	    'lua',
	    'm68k',
	    'magiksf',
	    'make',
	    'mapbasic',
	    'matlab',
	    'mirc',
	    'mmix',
	    'modula2',
	    'modula3',
	    '68000devpac',
	    'mpasm',
	    'mxml',
	    'mysql',
	    'newlisp',
	    'text',
	    'nsis',
	    'oberon2',
	    'objeck',
	    'objc',
	    'ocaml-brief',
	    'ocaml',
	    'pf',
	    'glsl',
	    'oobas',
	    'oracle11',
	    'oracle8',
	    'oz',
	    'pascal',
	    'pawn',
	    'pcre',
	    'per',
	    'perl',
	    'perl6',
	    'php',
	    'php-brief',
	    'pic16',
	    'pike',
	    'pixelbender',
	    'plsql',
	    'postgresql',
	    'povray',
	    'powershell',
	    'powerbuilder',
	    'proftpd',
	    'progress',
	    'prolog',
	    'properties',
	    'providex',
	    'purebasic',
	    'pycon',
	    'python',
	    'q',
	    'qbasic',
	    'rsplus',
	    'rails',
	    'rebol',
	    'reg',
	    'robots',
	    'rpmspec',
	    'ruby',
	    'gnuplot',
	    'sas',
	    'scala',
	    'scheme',
	    'scilab',
	    'sdlbasic',
	    'smalltalk',
	    'smarty',
	    'sql',
	    'systemverilog',
	    'tsql',
	    'tcl',
	    'teraterm',
	    'thinbasic',
	    'typoscript',
	    'unicon',
	    'uscript',
	    'vala',
	    'vbnet',
	    'verilog',
	    'vhdl',
	    'vim',
	    'visualprolog',
	    'vb',
	    'visualfoxpro',
	    'whitespace',
	    'whois',
	    'winbatch',
	    'xbasic',
	    'xml',
	    'xorg_conf',
	    'xpp',
	    'yaml',
	    'z80',
	    'zxbasic'
	]
