#!/usr/bin/env python3.4

import sqlite3

class Database:

	def __init__(self, path):
		self.conn = sqlite3.connect(path)
		self.path = path
		
		
	def createDB(self):
	
		c = self.conn.cursor()
	
		c.execute("DROP TABLE IF EXISTS activite")
		c.execute("CREATE TABLE activite (numero INTEGER, nom VARCHAR)")
		
		c.execute("DROP TABLE IF EXISTS equipement")
		c.execute("CREATE TABLE equipement (numero INTEGER, nom VARCHAR)")
		
		c.execute("DROP TABLE IF EXISTS installation")
		c.execute("CREATE TABLE installation (numero INTEGER, nom VARCHAR, adresse VARCHAR, code_postal INTEGER, ville VARCHAR, latitude DECIMAL, longitude DECIMAL)")

		self.conn.commit()

		
	def InsertInActivity(self, activite):
                c = self.conn.cursor()
		c.execute('''INSERT INTO activite(name, number) VALUES(:name, :number)''',
                          {'name':activite.name, 'number':activite.number})

		
	def InsertInEquipment(self, equipement):
		c = self.conn.cursor()
		c.execute('''INSERT INTO equipement(number, name, installationNumber) VALUES(:number, :name, :installationNumber) VALUES(:name, :number, :installationNumber)''',
                          {'number':equipement.number, 'name':equipement.name, 'installationNumber':equipement.installationNumber})

		
	def InsertInInstallation(self, installation):
		c = self.conn.cursor()
		c.execute('''INSERT INTO installation(number, name, address, zipCode, city, latitude, longitude) VALUES(:number, :name: address, :zipCode, :city, :latitude, :longitude)''',
                          {'number':installation.number, 'name':installation.name, 'address':installation.address, 'zipCode':installation.zipCode, 'city':installation.city, 'latitude':installation.latitude, 'longitude':installation.longitude})

	
	def commitDB(self):
		self.conn.commit()
		
	def disconnect(self):
	
		self.conn.close()
