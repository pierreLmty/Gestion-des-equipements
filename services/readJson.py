#!/usr/bin/env python3.4

import json

class ReadJson:

	def __init__(self, path):
		self.file = open(path)
		
	def read(self):
		data = json.load(self.file)
		
		for l in data["data"]:
			self.result.append(l)
		
	def getResult(self):
		return self.result
