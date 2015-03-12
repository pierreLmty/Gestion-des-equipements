#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

from services.readJson import ReadJSON
from services.database import Database
from model.activity import Activity
from model.equipment import Equipment
from model.installation import Installation

print("Creation of activity database...")
database = Database("data/activities.db")
database.createDB()
print("Database created")


print("Creation of equipment database...")
database = Database("data/equipments.db")
database.createDB()
print("Database created")


print("Creation of installation database...")
database = Database("data/installations.db")
database.createDB()
print("Database created")


print("Insertion in activity database...")
rdA = ReadJSON("data/activities.json")
rdA.readActivity()
resultA = rdA.getResult()
print("File read")

for i in resultA:
	database.InsertInActivity(i)
database.commitDB()
print("Insertion done")


print("Insertion in equipment database...")
rdE = ReadJSON("data/equipments.json")
rdE.readEquipment()
resultE = rdE.getResult()
print("File read")

for i in resultE:
        database.InsertInEquipment(i)
database.commitDB()
print("Insertion done")


print("Insertion in installation database...")
rdI = ReadJSON("data/installations.json")
rdI.readInstallation()
resultI = rdI.getResult()
print("File read")

for i in resultI:
        database.InsertInInstallation(i)
database.commitDB()
print("Insertion done")
