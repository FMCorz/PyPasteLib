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


class PastiePaster(BasePaster):

    _api = 'pastie.org'
    _uri = '/pastes'
    _method = 'POST'
    _ssl = False
    _defaultAuthorization = 'burger'
    _defaultSyntax = 'txt'

    def paste(self):
        data = {
            'paste[body]': self.prepare(),
            'paste[authorization]': self.prepate_authorization(),
            'paste[restricted]': self.prepare_private(),
        }

        syntax = self.prepare_syntax(id=True)
        if syntax:
            data['paste[parser_id]'] = syntax

        data = urllib.urlencode(data)
        headers = {'Content-type': 'application/x-www-form-urlencoded'}

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

        raise PasteFailed('Paste failed. Response: %s (%s). Expected: 302.' % (str(resp.status), str(resp.reason)))

    def prepate_authorization(self):
        return self.setting('authorization', self._defaultAuthorization)

    def prepare_syntax(self, syntax=None, id=False, **kwargs):
        s = super(PastiePaster, self).prepare_syntax(syntax=syntax, **kwargs)
        s = self.syntaxes[s]
        if id:
            return s[1]
        return s[0]

    def supportedSyntaxes(self):
        return self.syntaxes.keys()

    syntaxes = {
        'objc': ('objective-c++', 1),
        'as': ('actionscript', 2),
        'rb': ('ruby', 3),
        'ror': ('ruby_on_rails', 4),
        'diff': ('diff', 5),
        'txt': ('plain_text', 6),
        'cpp': ('c++', 7),
        'css': ('css', 8),
        'java': ('java', 9),
        'js': ('javascript', 10),
        'html': ('html', 11),
        'xml': ('html', 11),
        'erb': ('html_rails', 12),
        'sh': ('shell-unix-generic', 13),
        'sql': ('sql', 14),
        'php': ('php', 15),
        'py': ('python', 16),
        'pas': ('pascal', 17),
        'pl': ('perl', 18),
        'yml': ('yaml', 19),
        'cs': ('csharp', 20),
        'go': ('go', 21),
        'apache': ('apache', 22),
        'lua': ('lua', 23),
        'io': ('io', 24),
        'lisp': ('lisp', 25),
        'd': ('d', 26),
        'erl': ('erlang', 27),
        'f90': ('fortran', 28),
        'hs': ('haskell', 29),
        'lhs': ('literate_haskell', 30),
        'mak': ('makefile', 31),
        'scala': ('scala', 32),
        'scm': ('scheme', 33),
        'tpl': ('smarty', 34),
        'ini': ('ini', 35),
        'nu': ('nu', 36),
        'tex': ('tex', 37),
        'clj': ('clojure', 38),
        'pp': ('puppet', 39)
    }
