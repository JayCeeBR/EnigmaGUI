# -*- coding: latin1 -*-
import sqlite3

class Database(object):

	def __init__(self):
		self.connection = sqlite3.connect('enigmadb.db')
		self.cursor = self.connection.cursor()
		query = 'CREATE TABLE IF NOT EXISTS rotors (id integer primary key, rotorid varchar(100),base varchar(100))'
		self.cursor.execute(str(query))
		query = 'CREATE TABLE IF NOT EXISTS reflector (id integer primary key, reflectorid varchar(100),base varchar(100))'
		self.cursor.execute(str(query))

	def execute(self, query):
		try:
			self.cursor.execute(str(query))
		except Exception as e:
			print("{0}".format(e))

	def return_value(self, query):
		try:
			self.cursor.execute(str(query))
			output = self.cursor.fetchall()
			for row in output:
				return row['base'] 
		except Exception as e:
			print("{0}".format(e))

	def show(self, query):
		try:
			self.cursor.execute(str(query))
			showin = self.cursor.fetchall()
			for showme in showin:
				print('%d: %s(%s)' % showme)
		except Exception as e:
			print("{0}".format(e))

	def destroy_connection(self):
		self.connection.close()
