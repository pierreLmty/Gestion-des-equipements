#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

"""
This part of program is used to load JSON file in the database
"""

from services.readJson import ReadJSON
from services.database import Database
from model.activity import Activity
from model.equipment import Equipment
from model.installation import Installation
from progressbar import *

print("Creation of database...")
database = Database("data/database.db")
database.create_DB()
print("Database created")


print("Insertion in installation table...")
rdI = ReadJSON("data/installations.json")
rdI.readInstallation()
resultI = rdI.getResult()
print("File read")

progressBar = ProgressBar(widgets=['Writing installations to the database: ', Percentage(), ' ', ETA()])
for i in progressBar(resultI):
        database.Insert_In_Installation(i)
database.commit_DB()
print("Insertion done")


print("Insertion in equipment table...")
rdE = ReadJSON("data/equipments.json")
rdE.readEquipment()
resultE = rdE.getResult()
print("File read")

progressBar = ProgressBar(widgets=['Writing equipments to the database: ', Percentage(), ' ', ETA()])
for i in progressBar(resultE):
        database.Insert_In_Equipment(i)
database.commit_DB()
print("Insertion done")


print("Insertion in activity table...")
rdA = ReadJSON("data/activities.json")
rdA.readActivity()
resultA = rdA.getResult()
print("File read")

progressBar = ProgressBar(widgets=['Writing activities to the database: ', Percentage(), ' ', ETA()])
for i in progressBar(resultA):
	database.Prepare_Insert_In_Activity(i)
database.Insert_In_Activity()
database.commit_DB()
print("Insertion done")

print("All is done")
database.disconnect()
