#!/usr/bin/env python3.4

from services.database import Database

db = Database("data/installation.db", "installations")
db.createDB()
db.disconnect()

