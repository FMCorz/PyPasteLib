# -*- coding: utf-8 -*-

"""
PyPasteLib

A Python library to format and paste text.

Copyright (c) 2013 Frédéric Massart - FMCorz.net

Licensed under The MIT License
Redistributions of files must retain the above copyright notice.

http://github.com/FMCorz/PyPasteLib
"""

from base import BasePaster


class RawPaster(BasePaster):

    syntaxes = {}

    def paste(self):
        return self.prepare()

    def prepare(self):
        content = ''
        for t in self.texts():
            if t.get('identifier'):
                content += '## ' + str(t.get('identifier'))
                if t.get('syntax', False):
                    content += ' [%s]' % self.prepare_syntax(t.get('syntax'))
                content += '\n'
            i = 0
            for text in t.get('text').split('\n'):
                i += 1
                content += '%d: %s\n' % (i, text)
            content += '\n'
        return content.strip()
