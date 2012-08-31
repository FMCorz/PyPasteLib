# -*- coding: utf-8 -*-

import urllib
from base import BasePaster

class HeypasteitPaster(BasePaster):

	_host = 'www.heypasteit.com'
	_uri = '/perm-it'
	_method = 'POST'
	_ssl = False

	def paste(self):
		data = {
	    	'fakesecurity': '2453564',
	        'text': self.prepare()
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

		print resp.status, resp.reason
		return False

	syntaxes = []
