#!/usr/bin/env python3.4

"""
Function to read a JSON file
"""

import json
from model.activity import Activity
from model.equipment import Equipment
from model.installation import Installation

class ReadJSON:

	def __init__(self, path):
		self.path = open(path)
		self.result = []
		
		
	def readActivity(self):
		"""
		Read one activity and insert it in the database
		"""
		data = json.load(self.path)
		
		for row in data["data"]:
			self.result.append(Activity(row["EquipementId"], row["ActLib"], row["EquipementId"]))
		
			
	def readEquipment(self):
		"""
		Read one equipment and insert it in the database
		"""
		data = json.load(self.path)
		
		for row in data["data"]:
			self.result.append(Equipment(row["EquipementId"], row["EquNom"], row["InsNumeroInstall"]))
		
			
	def readInstallation(self):
		"""
		Read one installation and insert it in the database
		"""
		data = json.load(self.path)
		
		for row in data["data"]:
			self.result.append(Installation(row["InsNumeroInstall"], row["geo"]["name"], str(row["InsNoVoie"]) + " " + str(row["InsLibelleVoie"]), row["InsCodePostal"], row["ComLib"], row["Latitude"], row["Longitude"]))
		
		
	def getResult(self):
		return self.result
