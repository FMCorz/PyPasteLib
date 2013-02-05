# -*- coding: utf-8 -*-

"""
PyPasteLib

A Python library to format and paste text.

Copyright (c) 2013 Frédéric Massart - FMCorz.net

Licensed under The MIT License
Redistributions of files must retain the above copyright notice.

http://github.com/FMCorz/PyPasteLib
"""

import json
import urllib
from base import BasePaster


class KdePaster(BasePaster):

    _host = 'paste.kde.org'
    _uri = '/'
    _method = 'POST'
    _ssl = False

    def paste(self):
        data = {
            'paste_user': self.poster(),
            'paste_lang': self.prepare_syntax(keepWhenMissing=False),
            'paste_data': self.prepare(),
            'paste_private': self.prepare_private(),
            'paste_expire': self.prepare_ttl(),
            'paste_password': '',
            'api_submit': True,
            'mode': 'json'
        }
        data = urllib.urlencode(data)
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        (resp, d, h) = self.httpRequest(
                host=self._host,
                uri=self._uri,
                method=self._method,
                ssl=self._ssl,
                data=data,
                headers=headers
            )
        if resp.status == 200:
            try:
                url = 'http://%s/' % self._host
                data = json.loads(d).get('result', {})
                id = data.get('id', False)
                if not id:
                    raise Exception('Error during request')
                url += id
                hash = data.get('hash', None)
                if hash:
                    url += '/' + hash
            except:
                print data
                url = False
            return url

        print resp.status, resp.reason
        return False

    def prepare_ttl(self):
        ttl = self.ttl()
        if ttl <= 30:
            return 1800
        elif ttl <= 60 * 6:
            return 21600
        elif ttl <= 60 * 24:
            return 86400
        elif ttl <= 60 * 24 * 7:
            return 604800
        elif ttl <= 60 * 24 * 31:
            return 2592000
        else:
            return 0

    syntaxes = [
        'cpp',
        'diff',
        'gdb',
        'javascript',
        'text',
        'perl',
        'php',
        'python',
        'ruby',
        'xml',
        'abap',
        '6502acme',
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
        'bash',
        'basic4gl',
        'bf',
        'bibtex',
        'blitzbasic',
        'bnf',
        'boo',
        'c',
        'c_loadrunner',
        'c_mac',
        'caddcl',
        'cadlisp',
        'cfdg',
        'cfm',
        'chaiscript',
        'cil',
        'clojure',
        'cmake',
        'cobol',
        'cpp',
        'cpp-qt',
        'csharp',
        'css',
        'cuesheet',
        'd',
        'dcs',
        'delphi',
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
        'f1',
        'falcon',
        'fo',
        'fortran',
        'freebasic',
        'fsharp',
        '4cs',
        'gambas',
        'gdb',
        'genero',
        'genie',
        'gettext',
        'glsl',
        'gml',
        'gnuplot',
        'go',
        'groovy',
        'gwbasic',
        'haskell',
        'hicest',
        '68000devpac',
        'hq9plus',
        'html4strict',
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
        '6502kickass',
        'kixtart',
        'klonec',
        'klonecpp',
        'latex',
        'lb',
        'lisp',
        'locobasic',
        'logtalk',
        'lolcode',
        'lotusformulas',
        'lotusscript',
        'lscript',
        'lsl2',
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
        'mpasm',
        'mxml',
        'mysql',
        'newlisp',
        'nsis',
        'oberon2',
        'objc',
        'objeck',
        'ocaml',
        'ocaml-brief',
        'oobas',
        'oracle11',
        'oracle8',
        'oxygene',
        'oz',
        'pascal',
        'pcre',
        'per',
        'perl',
        'perl6',
        'pf',
        'php',
        'php-brief',
        'pic16',
        'pike',
        'pixelbender',
        'plsql',
        'postgresql',
        'povray',
        'powerbuilder',
        'powershell',
        'progress',
        'prolog',
        'properties',
        'providex',
        'purebasic',
        'python',
        'q',
        'qbasic',
        'rails',
        'rebol',
        'reg',
        'robots',
        'rpmspec',
        'rsplus',
        'ruby',
        'sas',
        'scala',
        'scheme',
        'scilab',
        'sdlbasic',
        'smalltalk',
        'smarty',
        'sql',
        'systemverilog',
        '6502tasm',
        'tcl',
        'teraterm',
        'text',
        'thinbasic',
        'tsql',
        'typoscript',
        'unicon',
        'vala',
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
        'xbasic',
        'xml',
        'xorg_conf',
        'xpp',
        'z80',
        'zxbasic'
    ]
