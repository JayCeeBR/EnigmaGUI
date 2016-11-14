# -*- coding: latin1 -*-
from database import *
import string
import sys
from enigma import *

class Security(object):

	reflector = []
	rotors = []
	plugboard = []

	def save_reflector(self, option):
		self.reflector.append(str(option))

	def get_reflector(self):
		try:
			return self.reflector[0]
		except:
			return "null"

	def save_rotors(self, option1, option2, option3):
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
		self.plugboard.append(str(p1))
		self.plugboard.append(str(p2))
		self.plugboard.append(str(p3))
		self.plugboard.append(str(p4))