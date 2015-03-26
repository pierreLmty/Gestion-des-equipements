#!/usr/bin/env python3.4

import sqlite3

class Database:


	def __init__(self, path):
		self.conn = sqlite3.connect(path)
		self.path = path
		
		
	def create_DB(self):
		"""
		
		"""
	
		c = self.conn.cursor()

		c.execute("DROP TABLE IF EXISTS installation")
		c.execute("CREATE TABLE installation (number INTEGER PRIMARY KEY, name VARCHAR, address VARCHAR, zipCode INTEGER, city VARCHAR, latitude DECIMAL, longitude DECIMAL)")

		c.execute("DROP TABLE IF EXISTS equipement")
		c.execute("CREATE TABLE equipement (number INTEGER PRIMARY KEY, name VARCHAR, installationNumber INTEGER, FOREIGN KEY(installationNumber) REFERENCES installation(number))")

		c.execute("DROP TABLE IF EXISTS activite")
		c.execute("CREATE TABLE activite (number INTEGER PRIMARY KEY, name VARCHAR)")
	
		c.execute("DROP TABLE IF EXISTS ep_ac")
		c.execute("CREATE TABLE ep_ac (number INTEGER, name VARCHAR, equipment_number INTEGER)")

		c.execute("DROP TABLE IF EXISTS equipement_activite")
		c.execute("CREATE TABLE equipement_activite (number_equipment INTEGER, number_activity INTEGER, FOREIGN KEY(number_equipment) REFERENCES equipement(number), FOREIGN KEY(number_activity) REFERENCES activite(number))")

		self.commit_DB()


	def Insert_In_Installation(self, installation):
		c = self.conn.cursor()
		c.execute('INSERT INTO installation(number, name, address, zipCode, city, latitude, longitude) VALUES(:number, :name, :address, :zipCode, :city, :latitude, :longitude)',
                          {'number':installation.number, 'name':installation.name, 'address':installation.address, 'zipCode':installation.zipCode, 'city':installation.city, 'latitude':installation.latitude, 'longitude':installation.longitude})


	def Insert_In_Equipment(self, equipement):
		c = self.conn.cursor()
		c.execute('INSERT INTO equipement(number, name, installationNumber) VALUES(:number, :name, :installationNumber)',
                          {'number':equipement.number, 'name':equipement.name, 'installationNumber':equipement.installationNumber})

		
	def Prepare_Insert_In_Activity(self, prep_activite):
		c = self.conn.cursor()
		c.execute('INSERT INTO ep_ac(number, name, equipment_number) VALUES(:number, :name, :equipment_number)',
                          {'number':prep_activite.number, 'name':prep_activite.name, 'equipment_number':prep_activite.equipment_number})

	def Insert_In_Activity(self):
		c = self.conn.cursor()
		c.execute('INSERT INTO activite(number, name) SELECT number, name FROM ep_ac GROUP BY number')
		c.execute('INSERT INTO equipement_activite(number_equipment, number_activity) SELECT equipment_number, number FROM ep_ac GROUP BY number')
		c.execute("DROP TABLE IF EXISTS ep_ac")
		
	
	def read_Installations(self):
		c = self.conn.cursor()
		c.execute('SELECT * FROM installation')
		result = c.fetchall()
		installations = []
		
		for i in result:
			installations.append(result(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
			
		return installations
		
	def read_Equipments(self):
		c = self.conn.cursor()
		c.execute('SELECT * FROM equipement')
		result = c.fetchall()
		equipements = []
		
		for e in result:
			equipements.append(result(e[0], e[1], e[2]))
			
		return equipements
		
	def read_Activities(self):
		c = self.conn.cursor()
		c.execute('SELECT * FROM activite')
		result = c.fetchall()
		activites = []
		
		for a in result:
			activites.append(result(a[0], a[1]))
			
		return activites
		
	
	def commit_DB(self):
		self.conn.commit()
	
	
	def disconnect(self):
		self.conn.close()
