from google.appengine.ext import db


class Site(db.Model):
	code = db.StringProperty()
	url = db.StringProperty()
	label = db.StringProperty()


class Feed(db.Model):
	site = db.ReferenceProperty(Site)
	url = db.StringProperty()
	label = db.StringProperty()
	last_scraped = db.DateTimeProperty()
	last_hash = db.StringProperty()


class Item(db.Model):
	site = db.ReferenceProperty(Site)
	url = db.StringProperty()
	title = db.StringProperty()
	category = db.StringProperty()
	byline = db.StringProperty()
	description = db.TextProperty()
	pub_date = db.DateTimeProperty()
