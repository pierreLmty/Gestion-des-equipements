#!/usr/bin/env python3.4

import sqlite3

class Database:

	def __init__(self, path, name):
		self.conn = sqlite3.connect(path)
		self.path = path
		self.name = name
		
		
	def createDB(self):
	
		c = self.conn.cursor()

		c.execute("DROP TABLE IF EXISTS " + self.name)
		c.execute("CREATE TABLE " + self.name + " (numero integer, nom text)")

		self.conn.commit()
	
	
	def disconnect(self):
	
		self.conn.close()
