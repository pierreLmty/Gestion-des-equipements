#!/usr/bin/env python3.4

import sqlite3
from model.activity import Activity
from model.equipment import Equipment
from model.installation import Installation

class Database:


	def __init__(self, path):
		self.conn = sqlite3.connect(path)
		self.path = path
		
		
	def create_DB(self):
		"""
		Creating different tables inside the database
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
		"""
		Insertion of installations in the installation table
		"""
		c = self.conn.cursor()
		c.execute('INSERT INTO installation(number, name, address, zipCode, city, latitude, longitude) VALUES(:number, :name, :address, :zipCode, :city, :latitude, :longitude)',
                          {'number':installation.number, 'name':installation.name, 'address':installation.address, 'zipCode':installation.zipCode, 'city':installation.city, 'latitude':installation.latitude, 'longitude':installation.longitude})


	def Insert_In_Equipment(self, equipement):
		"""
		Insertion of equipments in the equipment table
		"""
		c = self.conn.cursor()
		c.execute('INSERT INTO equipement(number, name, installationNumber) VALUES(:number, :name, :installationNumber)',
                          {'number':equipement.number, 'name':equipement.name, 'installationNumber':equipement.installationNumber})

		
	def Prepare_Insert_In_Activity(self, prep_activite):
		"""
		Preparation of insertion of activities in the activity table
		"""
		c = self.conn.cursor()
		c.execute('INSERT INTO ep_ac(number, name, equipment_number) VALUES(:number, :name, :equipment_number)',
                          {'number':prep_activite.number, 'name':prep_activite.name, 'equipment_number':prep_activite.equipment_number})


	def Insert_In_Activity(self):
		"""
		Insertion of activities in the activity table
		"""
		c = self.conn.cursor()
		c.execute('INSERT INTO activite(number, name) SELECT number, name FROM ep_ac GROUP BY number')
		c.execute('INSERT INTO equipement_activite(number_equipment, number_activity) SELECT equipment_number, number FROM ep_ac GROUP BY number')
		c.execute("DROP TABLE IF EXISTS ep_ac")
		
	
	def read_Installations(self):
		"""
		Reading of the entire installation table
		"""
		c = self.conn.cursor()
		c.execute('SELECT * FROM installation')
		result = c.fetchall()
		installations = []
		
		for i in result:
			installations.append(Installation(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
			
		return installations
		
		
	def read_Equipments(self):
		"""
		Reading of the entire installation table
		"""
		c = self.conn.cursor()
		c.execute('SELECT * FROM equipement')
		result = c.fetchall()
		equipements = []
		
		for e in result:
			equipements.append(Equipment(e[0], e[1], e[2]))
			
		return equipements
		
		
	def read_Activities(self):
		"""
		Reading of the entire installation table
		"""
		c = self.conn.cursor()
		c.execute('SELECT * FROM activite')
		result = c.fetchall()
		activites = []
		
		for a in result:
			activites.append(Activity(a[0], a[1], 0))
			
		return activites


	def read_One_Installation(self, number):
		"""
		Read the entry of the given number
		"""
		c = self.conn.cursor()
		c.execute('SELECT * FROM installation WHERE number = :givenNumber', {'givenNumber':number})
		result = c.fetchone()

		try:
			installation = Installation(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
		except:
			return "Il n'y a pas d'installation qui possède ce numéro"
		return installation


	def read_One_Equipment(self, number):
		"""
		Read the entry of the given number
		"""
		c = self.conn.cursor()
		c.execute('SELECT * FROM equipement WHERE number = :givenNumber', {'givenNumber':number})
		result = c.fetchone()

		try:
			equipement = Equipment(result[0], result[1], result[2])
		except:
			return "Il n'y a pas d'équipement qui possède ce numéro"
		return equipement


	def read_One_Activity(self, number):
		"""
		Read the entry of the given number
		"""
		c = self.conn.cursor()
		c.execute('SELECT * FROM activite WHERE number = :givenNumber', {'givenNumber':number})
		result = c.fetchone()

		try:
			activity = Activity(result[0], result[1], 0)
		except:
			return "Il n'y a pas d'activité qui possède ce numéro"
		return activity


	def read_Informations(self, activity, city):
		"""      
		Read information about a sport in a city
		"""
		c = self.conn.cursor()
		#c.execute("""SELECT i.number, i.name, e.number, e.name, a.number, a.name FROM installation i JOIN equipement e ON i.number = e.installationNumber JOIN equipement_activite ea ON e.number = ea.number_equipment JOIN activite a ON ea.number_activity = a.number WHERE i.city = ' + city + '  AND a.name LIKE '% + activity + %'""")
		c.execute("SELECT DISTINCT i.number, i.name, e.number, e.name, a.number, a.name FROM installation i, equipement e, equipement_activite ea, activite a WHERE i.number = e.installationNumber AND e.number = ea.number_equipment AND ea.number_activity = a.number AND i.city = ' + city + '  AND a.name LIKE '% + activity + %'""")
		result = c.fetchall()
		query = []
		
		for r in result:
			query.append(Installation(r[0], r[1]), Equipment(r[0], r[1]), Activity(r[0], r[1]))
			
		print(query)
		return query
		
	
	def commit_DB(self):
		"""
		Commit changes
		"""
		self.conn.commit()
	
	
	def disconnect(self):
		"""
		Disconnect the database
		"""
		self.conn.close()
