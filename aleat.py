#!/usr/bin/python

import webapp
import random


class aleat(webapp.webApp):
	def process(self, parsedRequest):
		link = str(random.randrange(123456789))
		print link
		return ("200 OK", "<html><body>" + "<a href='" + link + "'>Dame otra</a>" + 
                        "</body></html>")




	
if __name__ == "__main__":
	testAleat= aleat("localhost", 1234)
