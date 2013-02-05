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


class PasteePaster(BasePaster):

    _api = 'pastee.org'
    _uri = '/submit'
    _method = 'POST'
    _ssl = True

    def paste(self):
        data = {
            'lexer': self.prepare_syntax(),
            'content': self.prepare(),
            'ttl': self.ttl() * 60
        }

        if self.password():
            data['encrypt'] = 'checked'
            data['key'] = self.password()

        data = urllib.urlencode(data)
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'text/plain'
        }

        (resp, d, h) = self.httpRequest(
                host=self._api,
                uri=self._uri,
                method=self._method,
                ssl=self._ssl,
                data=data,
                headers=headers
            )

        # Success
        if resp.status == 302:
            return h.get('location', False)

        print resp.status, resp.reason
        return False

    syntaxes = [
        'c',
        'csharp',
        'cpp',
        'css',
        'diff',
        'html',
        'java',
        'js',
        'objective-c',
        'php',
        'perl',
        'python',
        'rb',
        'sql',
        'tex',
        'text',
        'xml',
        'as',
        'apacheconf',
        'bbcode',
        'bash',
        'bat',
        'befunge',
        'boo',
        'brainfuck',
        'common-lisp',
        'd',
        'dpatch',
        'control',
        'sourceslist',
        'delphi',
        'django',
        'dylan',
        'erb',
        'erlang',
        'fortran',
        'gas',
        'genshi',
        'genshitext',
        'pot',
        'groff',
        'haskell',
        'ini',
        'irc',
        'io',
        'jsp',
        'llvm',
        'lhs',
        'logtalk',
        'lua',
        'moocode',
        'basemake',
        'mako',
        'matlab',
        'matlabsession',
        'minid',
        'trac-wiki',
        'mupad',
        'mysql',
        'myghty',
        'numpy',
        'ocaml',
        'python3',
        'pytb',
        'pycon',
        'rhtml',
        'raw',
        'redcode',
        'rbcon',
        'splus',
        'scheme',
        'smalltalk',
        'smarty',
        'squidconf',
        'tcl',
        'tcsh',
        'vb.net',
        'vim',
        'xslt',
        'c-objdump',
        'cpp-objdump',
        'd-objdump',
        'objdump',
        'rst',
        'css+django',
        'css+genshitext',
        'css+mako',
        'css+myghty',
        'css+php',
        'css+erb',
        'css+smarty',
        'html+django',
        'html+genshi',
        'html+mako',
        'html+myghty',
        'html+php',
        'html+smarty',
        'js+django',
        'js+genshitext',
        'js+mako',
        'js+myghty',
        'js+php',
        'js+erb',
        'js+smarty',
        'xml+django',
        'xml+mako',
        'xml+myghty',
        'xml+php',
        'xml+erb',
        'xml+smarty'
    ]
