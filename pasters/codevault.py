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
from exceptions import *


class CodevaultPaster(BasePaster):

    _host = 'cdv.lt'
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
            return 'http://' + self._host + h.get('location', False)

        raise PasteFailed('Paste failed. Response: %s (%s). Expected: 302.' % (str(resp.status), str(resp.reason)))

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
