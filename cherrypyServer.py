#!/usr/bin/env python3.4

import cherrypy
from services.database import Database
from model.activity import Activity
from model.equipment import Equipment
from model.installation import Installation


class WebManager(object):

	def add_HTML_header(self, title):
		header = '''<!DOCTYPE html>\n
				<html>\n
					<head>\n
						<title>''' + title + '''</title>\n
						<meta charset="utf-8"/>\n
					</head>\n
				<body>'''
		return header
		
	

	def add_HTML_footer(self):
		return '''</body>\n
			</html>'''
	
	
	@cherrypy.expose
	def index(self):
		"""
		Exposes the service at localhost:8080/
		"""
		html = self.add_HTML_header('Accueil')
		html += '''<h1>Installations Sportives des Pays de la Loire</h1>\n'''
		'''Code à mettre ? table?'''
		html += self.add_HTML_footer()
		return html
		
	
	@cherrypy.expose
	def display_Installations(self):
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

'''<a href="show_installations">Voir les installations</a><br/>\n'''
cherrypy.quickstart(WebManager())
