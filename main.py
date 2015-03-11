#!/usr/bin/env python3.4

from services.readJson import ReadJSON
from services.database import Database
from model.activity import Activity
from model.equipment import Equipment
from model.installation import Installation

"""
rdA = ReadJSON("data/activities.json")
rdA.readActivity()
resultA = rdA.getResult()

for row in resultA:
	print(str(row.number) + " ; " + str(row.name))
"""

"""	
rdE = ReadJSON("data/equipments.json")
rdE.readEquipment()
resultE = rdE.getResult()

for row in resultE:
	print(str(row.number) + " ; " + str(row.name))
"""

"""	
rdI = ReadJSON("data/installations.json")
rdI.readInstallation()
resultI = rdI.getResult()

for row in resultI:
	print(str(row.number) + " ; " + str(row.name) + " ; " + str(row.address) + " ; " + str(row.zipCode) + " ; " + str(row.city) + " ; " + str(row.latitude) + " ; " + str(row.longitude))
"""

print("Creation of activity database...")
database = Database("data/activities.json")
database.createDB()
print("Database created")

print("Creation of equipment database...")
database = Database("data/equipments.json")
database.createDB()
print("Database created")

print("Creation of installation database...")
database = Database("data/installations.json")
database.createDB()
print("Database created")

print("insertion in activity database...")
rdA = ReadJSON()
rdA.readActivity("data/Activites.json")
resultA = rdA.getResult()
print("File read")

for i in resultA:
	database.InsertInActivity(i)
database.commit()
print("Insertion done")

print("insertion in equipment database...")
database.InsertInEquipment()
print("Insertion done")

print("insertion in installation database...")
database.InsertInInstallation()
print("Insertion done")
