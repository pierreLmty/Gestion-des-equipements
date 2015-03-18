#!/usr/bin/env python3.4

import cherrypy
from servives.database import Database


class WebManager(object):

	def add_HTML_header(self, title):
		header = '''<!DOCTYPE html>\n<html>\n
		<head>\n<title>''' + title + '''</title>\n<meta charset="utf-8"/>\n</head>\n
		<body>'''
		return header

	def add_HTML_footer(self):
		return '</body>\n</html>'


cherrypy.quickstart(WebManager())
