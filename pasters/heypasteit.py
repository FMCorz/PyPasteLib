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


class HeypasteitPaster(BasePaster):

    _host = 'www.heypasteit.com'
    _uri = '/perm-it'
    _method = 'POST'
    _ssl = False

    def paste(self):
        data = {
            'fakesecurity': '2453564',
            'text': self.prepare().decode('utf-8').encode('iso-8859-15')
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
        if resp.status == 200 and not d.startswith('Error'):
            return 'http://' + self._host + '/clip/' + d.strip()

        raise PasteFailed('Paste failed. Response: %s (%s).' % (str(resp.status), str(resp.reason)))

    syntaxes = []
