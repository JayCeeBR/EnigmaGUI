# -*- coding: latin1 -*-
from database import *
import string
import sys
from enigma import *
import json

class Security(object):

	reflector = []
	rotors = []
	plugboard = []


	rotor1 = ""
	rotor2 = ""
	rotor3 = ""

	reflectorthis = ""

	def load_settings(self):
		try:
			with open('settings.json') as jdata:
				data = json.load(jdata)
				for out in data['Settings']:
					self.reflector.append(str(out['reflector']))
					self.rotors.append(str(out['rotor1']))
					self.rotors.append(str(out['rotor2']))
					self.rotors.append(str(out['rotor3']))
					self.plugboard.append(str(out['pair1-1']))
					self.plugboard.append(str(out['pair1-2']))
					self.plugboard.append(str(out['pair2-1']))
					self.plugboard.append(str(out['pair2-2']))
		except Exception as e:
			print("{0}".format(e))

	def save_reflector(self, option):
		self.reflector.clear()
		self.reflector.append(str(option))

	def get_reflector(self):
		try:
			return self.reflector[0]
		except:
			return "null"

	def save_rotors(self, option1, option2, option3):
		self.rotors.clear()
		self.rotors.append(str(option1))
		self.rotors.append(str(option2))
		self.rotors.append(str(option3))

	def get_rotors(self, option):
		try:
			if option == 1:
				return self.rotors[0]
			elif option == 2:
				return self.rotors[1]
			elif option == 3:
				return self.rotors[2]
		except Exception as e:
			return "null"

	def get_plugboard(self, option):
		try:
			if option == 1:
				return self.plugboard[0]
			elif option == 2:
				return self.plugboard[1]
			elif option == 3:
				return self.plugboard[2]
			elif option == 4:
				return self.plugboard[3]
		except Exception as e:
			return "null"

	def save_plugboard(self, p1, p2, p3, p4):
		self.plugboard.clear()
		self.plugboard.append(str(p1))
		self.plugboard.append(str(p2))
		self.plugboard.append(str(p3))
		self.plugboard.append(str(p4))


	def get_rotor1(self):
		return Database().return_value("SELECT base FROM rotors WHERE rotorid = '{0}'".format(self.rotors[0]))

	def get_rotor2(self):
		return Database().return_value("SELECT base FROM rotors WHERE rotorid = '{0}'".format(self.rotors[1]))

	def get_rotor3(self):
		return Database().return_value("SELECT base FROM rotors WHERE rotorid = '{0}'".format(self.rotors[2]))

	def get_reflector(self):
		return Database().return_value("SELECT base FROM reflector WHERE reflectorid = '{0}'".format(self.reflector[0]))

	def get_plugboard(self):
		return self.plugboard	