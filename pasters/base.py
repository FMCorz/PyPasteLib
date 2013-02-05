# -*- coding: utf-8 -*-

"""
PyPasteLib

A Python library to format and paste text.

Copyright (c) 2013 Frédéric Massart - FMCorz.net

Licensed under The MIT License
Redistributions of files must retain the above copyright notice.

http://github.com/FMCorz/PyPasteLib
"""

import httplib


class BasePaster(object):

    # To be implemented by any paster, must be a dict
    syntaxes = None

    # Protected variables
    _texts = None
    _private = None
    _description = None
    _poster = None
    _settings = None
    _syntax = None
    _ttl = None
    _password = None
    _defaultSyntax = 'txt'

    def __init__(self, **kwargs):
        self.reset()
        self.description(kwargs.get('description'))
        self.poster(kwargs.get('poster'))
        self.syntax(kwargs.get('syntax'))
        self.private(kwargs.get('private'))
        self.ttl(kwargs.get('ttl'))
        self.password(kwargs.get('password'))
        self._settings = kwargs.get('settings', {})
        self._buildTranslationTable()

    def add(self, text, identifier=None, syntax=None):
        """Adds a new blob to the paste"""
        if type(text) != unicode:
            text = unicode(text, 'utf-8')
        t = {
            "text": text.encode('utf-8'),
            "identifier": identifier,
            "syntax": syntax
        }
        self._texts.append(t)
        self.syntax(syntax)

    def description(self, desc=None):
        """Set/get the description of the paste"""
        if desc == None:
            return self._description
        self._description = desc

    def httpRequest(self, method='post', ssl=False, host=None, uri=None, data=None, headers=None, readData=True):
        """This method should not be called directly, but from within a plugin.
        host and uri parameters are required.
        data has to be formatted/escaped as required per your request.
        headers is a dict key/value.
        returns an tuple containing in order:
            - the HTTPResponse object
            - the data received
            - the headers
        """

        if host == None or uri == None:
            raise Exception('Missing required parameter')

        if ssl:
            r = httplib.HTTPSConnection(host)
        else:
            r = httplib.HTTPConnection(host)
        r.request(method.upper(), uri, data, headers if headers != None else {})

        resp = r.getresponse()
        data = None
        if readData:
            data = resp.read()

        respHeaders = {}
        for hkey, hvalue in resp.getheaders():
            respHeaders[hkey] = hvalue

        return (resp, data, respHeaders)

    def paste(self):
        """Contains the logic to post the content, you can use the httpRequest method
        to make your life easier.
        """
        return self.prepare()

    def password(self, password=None):
        """Set/get the password to access/encrypt the paste"""
        if password == None:
            return self._password
        self._password = password

    def poster(self, poster=None):
        """Set/get the poster of the paste"""
        if poster == None:
            return self._poster
        self._poster = poster

    def prepare(self):
        """Formats the content to be sent."""
        content = ''
        for t in self.texts():
            if t.get('identifier'):
                content += '## ' + str(t.get('identifier'))
                if t.get('syntax'):
                    content += ' [%s]' % self.prepare_syntax(t.get('syntax'), keepWhenMissing=True)
                content += '\n'
            content += t.get('text')
            content += '\n\n'
        return content.strip()

    def prepare_private(self):
        """Formats the private status to send to the paster.
        This is likely to be extended.
        """
        return 1 if self.private() else 0

    def prepare_syntax(self, syntax=None, keepWhenMissing=True):
        """Formats the syntax to be used to send to the paster."""
        if syntax == None:
            syntax = self.syntax()
        if syntax in self.supportedSyntaxes():
            return syntax
        elif syntax in self._translationTable.keys():
            for alias in self._translationTable[syntax]:
                if alias in self.supportedSyntaxes():
                    return alias
        return syntax if keepWhenMissing else self.prepare_syntax(keepWhenMissing=True, syntax=self._defaultSyntax)

    def private(self, private=None):
        """Set/get the privacy of the paste"""
        if private == None:
            return self._private
        self._private = private

    def reset(self):
        """Resets to default"""
        self._texts = []
        self._poster = 'Anonymous'
        self._private = False
        self._description = ''
        self._syntax = None
        self._ttl = 60 * 24 * 30
        self._password = None

    def setting(self, name, default=None):
        """Reads the plugin settings"""
        return self._settings.get(name, default)

    def supportedSyntaxes(self):
        """Returns the syntaxes supported by the plugin"""
        return self.syntaxes

    def syntax(self, syntax=None):
        """Set/get the global syntax"""
        if syntax == None:
            return self._syntax if self._syntax != None else self._defaultSyntax
        self._syntax = syntax.lower()

    def texts(self):
        """Returns the blobs set"""
        return self._texts

    def ttl(self, ttl=None):
        """Set/get the time to live in minutes of the paste"""
        if ttl == None:
            return self._ttl
        self._ttl = ttl

    def _buildTranslationTable(self):
        """Builds the syntax translation table"""
        tt = {}
        for aliases in self._aliases:
            for alias in aliases:
                if tt.get(alias, False) != False:
                    raise Exception('Conflict in translation table. %s already defined.' % alias)
                tt[alias] = list(aliases)
                tt[alias].remove(alias)
        self._translationTable = tt

    _translationTable = None
    _aliases = [
        ['c', 'cpp', 'c++'],
        ['javascript', 'js', 'jquery'],
        ['text', 'txt', 'plain_text', 'plain'],
        ['objectivec', 'objective-c', 'objc', 'm'],
        ['actionscript', 'as', 'actionscript3', 'as3'],
        ['ruby', 'rb', 'ror', 'ruby_on_rails', 'erb'],
        ['html', 'xml', 'htm', 'html4strict'],
        ['shell', 'sh', 'bash'],
        ['python', 'py'],
        ['pascal', 'pas'],
        ['perl', 'pl'],
        ['yaml', 'yml'],
        ['csharp', 'cs'],
        ['apache', 'apacheconf']
    ]
