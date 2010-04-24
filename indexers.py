import hashlib
import datetime
import logging
import datetime

from google.appengine.ext import webapp
from google.appengine.api.labs import taskqueue
from google.appengine.api import urlfetch

import parsedatetime as pdt


import helpers
import models




class FeedQueueHandler(webapp.RequestHandler):
	def get(self, sitecode):
		site = models.Site.get_by_key_name(sitecode)
		feeds = models.Feed.all().filter('site =', site)
		for feed in feeds:
			taskqueue.add(url='/index/feed', params={'page': "1", "url":feed.url}, method='GET')
			self.response.out.write(feed.url)
			self.response.out.write("<br />")


class FeedHandler(webapp.RequestHandler):
	def get(self):
		p = pdt.Calendar()
		url = self.request.get("url")
		if self.request.get("page"):
			page = self.request.get("page")
		else: 
			page = "1"
		pagesize = 3
		low = ((int(page) - 1) * pagesize) + 1
		high = int(page) * pagesize
		query = "select title, link, description, category.content, creator, pubDate, link from rss where url='"+ url +"'"
		result = helpers.do_yql(query)
		self.response.out.write(url)
		self.response.out.write("<br />")
		feed = models.Feed.get_by_key_name(url)
		self.response.out.write(feed.site.code)
		self.response.out.write("<br />")
		resulthash = hashlib.md5(str(result)).hexdigest()
		feed.last_hash = resulthash
		feed.last_scraped = datetime.datetime.today()
		self.response.out.write(resulthash)
		self.response.out.write("<br />")
		self.response.out.write("<br />")
		self.response.out.write(str(low) + "/" + str(high))
		self.response.out.write("<br />")
		self.response.out.write("<br />")
		index = True
		i = 0
		for element in result['query']['results']['item']:
			i += 1
			try:
				if i <= high and i >= low:
					self.response.out.write(i)
					self.response.out.write("<br />")
					category = ""
					description = ""
					title = ""
					pub_date = ""
					creator = ""
					link = ""
					try:
						category = element['category']
						self.response.out.write(element['category'])
						self.response.out.write("<br />")
					except:
						error = True
					try:
						if not "img" in element['description']:
							description = element['description']
							self.response.out.write(element['description'])
							self.response.out.write("<br />")
					except:
						error = True
					try:
						title = element['title']
						self.response.out.write(element['title'])
						self.response.out.write("<br />")
					except:
						error = True
					try:
						self.response.out.write(element['pubDate'])
						self.response.out.write("<br />")
						pub_date = datetime(p.parse(element['pubDate']))
						self.response.out.write(pub_date)
						self.response.out.write("<br />")
					except:
						error = True
					try:
						creator = element['creator'].title()
						self.response.out.write(element['creator'].title())
						self.response.out.write("<br />")
					except:
						error = True
					try:
						self.response.out.write(element['link'])
						if "phdo" in str(element['link']):
							lookup = urlfetch.fetch(element['link'])
							self.response.out.write("<br />")
							self.response.out.write(lookup.status_code)
							self.response.out.write("<br />")
							self.response.out.write(lookup.final_url)
							self.response.out.write("<br />")
							link = lookup.final_url
						else:
							link = element['link']
						if feed.site.code == "nyt":
							link = link.replace("?partner=rss&emc=rss", "")
						elif feed.site.code == "wsj":
							link, sep, discard = link.partition("?mod")
						elif feed.site.code == "sfc":
							link, sep, discard = link.partition("&feed")
						elif feed.site.code == "wp":
							link = link.replace("?nav=rss_email/components", "")
						else:
							self.response.out.write("unknown url")
						self.response.out.write(link)
						self.response.out.write("<br />")
						self.response.out.write("Now to persist")
						self.response.out.write("<br />")
						item = models.Item.get_or_insert(url, site=feed.site, url=link, title=title, category=category, description=description, byline=creator, pub_date=pub_date)
					except:
						temp = True
						self.response.out.write("failed to persist")
						self.response.out.write("<br />")
			except:
				self.response.out.write(element)
		self.response.out.write("<br />")
		if i > high:
			taskqueue.add(url='/index/feed', params={'page': str(int(page) + 1), "url":url}, method='GET')
		feed.put()
