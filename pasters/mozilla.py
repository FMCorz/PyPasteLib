# -*- coding: utf-8 -*-

"""
PyPasteLib

A Python library to format and paste text.

Copyright (c) 2013 Frédéric Massart - FMCorz.net

Licensed under The MIT License
Redistributions of files must retain the above copyright notice.

http://github.com/FMCorz/PyPasteLib
"""

import urllib
from base import BasePaster


class MozillaPaster(BasePaster):

    _host = 'pastebin.mozilla.org'
    _uri = '/'
    _method = 'POST'
    _ssl = False

    def paste(self):
        data = {
            'poster': self.poster(),
            'format': self.prepare_syntax(keepWhenMissing=False),
            'expiry': self.prepare_ttl(),
            'code2': self.prepare(),
            'paste': 'Send',
            'parent_pid': ''
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
        if resp.status == 302:
            return h.get('location', False)

        print resp.status, resp.reason
        return False

    def prepare_ttl(self):
        ttl = self.ttl()
        if ttl <= 60 * 24:
            return 'd'
        elif ttl <= 60 * 24 * 31:
            return 'm'
        else:
            return 'f'

    syntaxes = [
        'bash',
        'c',
        'cpp',
        'html4strict',
        'java',
        'javascript',
        'lua',
        'perl',
        'php',
        'python',
        'ruby',
        'text',
        'actionscript',
        'ada',
        'apache',
        'applescript',
        'asm',
        'asp',
        'bash',
        'c',
        'c_mac',
        'caddcl',
        'cadlisp',
        'cpp',
        'csharp',
        'cfm',
        'css',
        'd',
        'delphi',
        'diff',
        'dos',
        'eiffel',
        'fortran',
        'freebasic',
        'gml',
        'html4strict',
        'ini',
        'java',
        'javascript',
        'lisp',
        'lua',
        'matlab',
        'mpasm',
        'mysql',
        'nsis',
        'objc',
        'ocaml',
        'oobas',
        'oracle8',
        'pascal',
        'perl',
        'php',
        'python',
        'qbasic',
        'robots',
        'ruby',
        'scheme',
        'smarty',
        'sql',
        'tcl',
        'vb',
        'vbnet',
        'visualfoxpro',
        'xml'
    ]
