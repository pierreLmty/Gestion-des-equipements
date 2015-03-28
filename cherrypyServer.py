#!/usr/bin/env python3.4

import cherrypy
from services.database import Database
from model.activity import Activity
from model.equipment import Equipment
from model.installation import Installation
from mako.template import Template
from mako.lookup import TemplateLookup


class WebManager(object):

	def add_HTML_header(self, title):
		header = '''<!DOCTYPE html>
				<html>
					<head>
						<title>''' + title + '''</title>
						<meta charset="utf-8"/>
                                                <link rel="stylesheet" type="text/css" href="style/style.css"/>
					</head>
				<body>'''
		return header
		
	

	def add_HTML_footer(self):
		return '''</body>
			</html>'''
	
	
	@cherrypy.expose
	def index(self):
		"""
		Exposes the service at localhost:8080/
		"""
		html = self.add_HTML_header('Accueil')

		html += '''<h1>Installations sportives de la région des Pays de la Loire</h1>
                <fieldset>
                <legend>Afficher l'ensemble des données</legend>
                <input type="button" name="Installation" value="Afficher les installations" onclick="self.location.href='display_Installations'">
                <input type="button" name="Equipements" value="Afficher les équipements" onclick="self.location.href='display_Equipments'">
                <input type="button" name="Activites" value="Afficher les activités" onclick="self.location.href='display_Activities'">
                </fieldset>

                <form method="POST" action="query">
		        <fieldset>
		        <legend>Rechercher un sport dans une ville</legend>
				<input type="text" name="sport" placeholder="Rechercher un sport">
				<input type="text" name="ville" placeholder="Rechercher dans une ville">
				<input type="submit" name="search" value="rechercher">
		        </fieldset>
                </form>
                '''
		
		html += self.add_HTML_footer()
		return html
		
	
	@cherrypy.expose
	def display_Installations(self):
		"""
		Displays all installations
		"""
		html = self.add_HTML_header('Installations')
		database = Database('data/database.db')
		insts = database.read_Installations()
		html += '''<h2>Tableau des installations</h2>\n
			 <table>\n
			 	<tr>\n
			 		<th>Numéro</th>\n
			 		<th>Nom</th>\n
			 		<th>Adresse</th>\n
			 		<th>Code postal</th>\n
			 		<th>Ville</th>\n
			 		<th>Latitude</th>\n
			 		<th>Longitude</th>\n
			 	</tr>\n'''
		for i in insts:
			html += '''<tr>\n
					<td>''' + str(i.number) + '''</td>\n
					<td>''' + i.name + '''</td>\n
					<td>''' + i.address + '''</td>\n
					<td>''' + str(i.zipCode) + '''</td>\n
					<td>''' + i.city + '''</td>\n
					<td>''' + str(i.latitude) + '''</td>\n
					<td>''' + str(i.longitude) + '''</td>\n
				</tr>\n'''
		html += '''</table>\n'''
		return html


	@cherrypy.expose
	def display_Equipments(self):
		"""
		Displays all equipments
		"""
		html = self.add_HTML_header('Equipements')
		database = Database('data/database.db')
		equips = database.read_Equipments()
		html += '''<h2>Tableau des équipements</h2>\n
			<table>\n
				<tr>\n
					<th>Numéro</th>\n
					<th>Nom</th>\n
					<th>Numéro de l'installation</th>\n
				</tr>\n'''
		for e in equips:
			html += '''<tr>\n
					<td>''' + str(e.number) + '''</td>\n
					<td>''' + e.name + '''</td>\n
					<td>''' + str(e.installationNumber) + '''</td>\n
				</tr>\n'''
		html += '''</table>\n'''
		return html
		
	
	@cherrypy.expose	
	def display_Activities(self):
		"""
		Displays all activities
		"""
		html = self.add_HTML_header('Activités')
		database = Database('data/database.db')
		acts = database.read_Activities()
		html += '''<h2>Tableau des activitiés</h2>\n
			<table>\n
				<tr>\n
					<th>Numéro</th>\n
					<th>Nom</th>\n
				</tr>\n'''
		for a in acts:
			html += '''<tr>\n
					<td>''' + str(a.number) + '''</td>\n
					<td>''' + str(a.name) + '''</td>\n
				</tr>\n'''
		html += '''</table>\n'''
		return html


cherrypy.quickstart(WebManager())
