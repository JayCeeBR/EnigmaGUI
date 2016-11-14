# -*- coding: latin1 -*-
from database import *
import string
import sys
from enigma import *

class Security(object):

	reflector = []
	rotors = []

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