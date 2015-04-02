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
		"""
		Add the html header
		"""
		header = '''<!DOCTYPE html>
				<html>
					<head>
						<title>''' + title + '''</title>
						<meta charset="utf-8"/>
					</head>
				<body>'''
		return header
		

	def add_HTML_footer(self):
		"""
		Add the html footer
		"""
		return '''</body>
			</html>'''
	
	
	@cherrypy.expose
	def index(self):
		"""
		Exposes the service at localhost:8080/
		"""
		html = self.add_HTML_header('Accueil')
		temp = Template(filename="include/index.html")
		css = Template(filename="include/css.html")
		html += (css.render())
		html += (temp.render())
		
		html += self.add_HTML_footer()
		return html
		
	
	@cherrypy.expose
	def display_Installations(self):
		"""
		Displays all installations
		"""
		html = self.add_HTML_header('Installations')
		css = Template(filename="include/css.html")
		html += (css.render())
		database = Database('data/database.db')
		insts = database.read_Installations()
		html += '''<h2>Tableau des installations</h2>
			 <table border=1>
			 	<tr>
			 		<th>Numéro</th>
			 		<th>Nom</th>
			 		<th>Adresse</th>
			 		<th>Code postal</th>
			 		<th>Ville</th>
			 		<th>Latitude</th>
			 		<th>Longitude</th>
			 	</tr>\n'''
		for i in insts:
			html += '''<tr>\n
					<td>''' + str(i.number) + '''</td>
					<td>''' + i.name + '''</td>
					<td>''' + i.address + '''</td>
					<td>''' + str(i.zipCode) + '''</td>
					<td>''' + i.city + '''</td>
					<td>''' + str(i.latitude) + '''</td>
					<td>''' + str(i.longitude) + '''</td>
				</tr>'''
		html += '''</table>'''
		return html


	@cherrypy.expose
	def display_Equipments(self):
		"""
		Displays all equipments
		"""
		html = self.add_HTML_header('Equipements')
		css = Template(filename="include/css.html")
		html += (css.render())
		database = Database('data/database.db')
		equips = database.read_Equipments()
		html += '''<h2>Tableau des équipements</h2>
			<table border=1>
				<tr>
					<th>Numéro</th>
					<th>Nom</th>
					<th>Numéro de l'installation</th>
				</tr>'''
		for e in equips:
			html += '''<tr>
					<td>''' + str(e.number) + '''</td>
					<td>''' + e.name + '''</td>
					<td>''' + str(e.installationNumber) + '''</td>
				</tr>'''
		html += '''</table>'''
		return html
		
	
	@cherrypy.expose	
	def display_Activities(self):
		"""
		Displays all activities
		"""
		html = self.add_HTML_header('Activités')
		css = Template(filename="include/css.html")
		html += (css.render())
		database = Database('data/database.db')
		acts = database.read_Activities()
		html += '''<h2>Tableau des activitiés</h2>
			<table border=1>
				<tr>
					<th>Numéro</th>
					<th>Nom</th>
				</tr>'''
		for a in acts:
			html += '''<tr>
					<td>''' + str(a.number) + '''</td>
					<td>''' + str(a.name) + '''</td>
				</tr>'''
		html += '''</table>'''
		return html

                
	@cherrypy.expose
	def display_One_Installation(self, number):
		"""
		Display one installation
		"""
		html = self.add_HTML_header('Installations ' + number)
		css = Template(filename="include/css.html")
		html += (css.render())
		database = Database('data/database.db')
		inst = database.read_One_Installation(number)
		html += '''<h2>Installation n°''' + number + '''</h2>
			<table border=1>
				<tr>
					<th>Numéro</th>
					<th>Nom</th>
					<th>Adresse</th>
					<th>Code postal</th>
					<th>Ville</th>
					<th>Latitude</th>
					<th>Longitude</th>
				</tr>'''
                
		html += '''<tr>
				<td>''' + str(inst.number) + '''</td>
				<td>''' + inst.name + '''</td>
				<td>''' + inst.address + '''</td>
				<td>''' + str(inst.zipCode) + '''</td>
				<td>''' + inst.city + '''</td>
				<td>''' + str(inst.latitude) + '''</td>
				<td>''' + str(inst.longitude) + '''</td>
			</tr>'''
		html += '''</table>'''
		return html
		
                
	@cherrypy.expose
	def display_One_Equipment(self, number):
		"""
		Display one equipment
		"""
		html = self.add_HTML_header('Equipement ' + number)
		css = Template(filename="include/css.html")
		html += (css.render())
		database = Database('data/database.db')
		equip = database.read_One_Equipment(number)
		html += '''<h2>Equipement n°''' + number + '''</h2>
			<table border=1>
				<tr>
					<th>Numéro</th>
					<th>Nom</th>
					<th>Numéro de l'installation</th>
				</tr>'''
                
		html += '''<tr>
				<td>''' + str(equip.number) + '''</td>
				<td>''' + equip.name + '''</td>
				<td>''' + str(equip.installationNumber) + '''</td>
			</tr>'''
		html += '''</table>'''
		return html
		

	@cherrypy.expose
	def display_One_Activity(self, number):
		"""
		Display one activity
		"""
		html = self.add_HTML_header('Activité ' + number)
		css = Template(filename="include/css.html")
		html += (css.render())
		database = Database('data/database.db')
		act = database.read_One_Activity(number)
		html += '''<h2>Activité n°''' + number + '''</h2>
			<table border=1>
				<tr>
					<th>Numéro</th>
					<th>Nom</th>
				</tr>'''
                
		html += '''<tr>
				<td>''' + str(act.number) + '''</td>
				<td>''' + act.name + '''</td>
			</tr>'''
		html += '''</table>'''
		return html


	@cherrypy.expose
	def display_Informations(self, activity, city):
		"""
		Display informations about an activity and a city
		"""
		html = self.add_HTML_header("Recherche de l'activité " + activity + " dans " + city)
		css = Template(filename="include/css.html")
		html += (css.render())
		database = Database('data/database.db')
		query = database.read_Informations(activity, city)
		html += '''<h2>Résultat de la recherche</h2>
			<table border=1>
				<tr>
					<th>Numéro de l'installation</th>
					<th>Nom de l'installation</th>
					<th>Numéro de l'équipement</th>
					<th>Nom de l'équipement</th>
					<th>Numéro de l'activité</th>
					<th>Nom de l'activité</th>
				</tr>'''
                
		html += '''<tr>'''
		for q in query:
			html += '''<td>''' + q[0].number + '''</td>'''
			html += '''<td>''' + q[1].name + '''</td>'''
				#<td>''' + query[0].number + '''</td>
				#<td>''' + query[0].name + '''</td>
				#<td>''' + query[1].number + '''</td>
				#<td>''' + query[1].name + '''</td>
				#<td>''' + query[2].number + '''</td>
				#<td>''' + query[2].name + '''</td>
		html +=	'''</tr>'''
		html += '''</table>'''
		return html


cherrypy.quickstart(WebManager())
