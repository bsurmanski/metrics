import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('hello world!')

app = webapp2.WSGIApplication([('/rest/hello', MainPage)], debug=True)
