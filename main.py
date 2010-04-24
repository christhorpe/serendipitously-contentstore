#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import re
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch


import BeautifulSoup

import loaders
import indexers


class MainHandler(webapp.RequestHandler):
	def get(self):
		self.response.out.write('Hello world!')



class TestHandler(webapp.RequestHandler):
	def get(self):
		html = urlfetch.fetch(self.request.get("url"))
		page = BeautifulSoup.BeautifulSoup(html.content)
		metadata = []
		for meta in page.findAll('meta', {'property' : re.compile(r'og:[a-z]+$')}):
			for attr, value in meta.attrs:
				metadata.append({attr:value})
 		self.response.out.write(metadata)


def main():
	application = webapp.WSGIApplication([
		('/', MainHandler),
		('/test', TestHandler),
		('/load/(.*)', loaders.LoadSiteFeeds),
		('/index/queue/(.*)', indexers.FeedQueueHandler),
		('/index/feed', indexers.FeedHandler),
		],debug=True)
	util.run_wsgi_app(application)


if __name__ == '__main__':
	main()
