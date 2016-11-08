# -*- coding: latin1 -*-
from tkinter import *


class Window(object):

	def __init__(self):
		self.window = Tk()
		self.window.minsize(800,600)
		self.window.maxsize(800,600)
		self.window.title("Enigma")

		self.menubar = Menu(self.window)
		self.settings = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Menu", menu=self.settings)
		self.settings.add_command(label="Configure Rotors", command=self.create_rotors)
		self.settings.add_command(label="Configure Plugboard", command=self.create_plugboard)
		self.settings.add_command(label="Configure Reflector", command=self.create_reflector)
		self.settings.add_separator()
		self.settings.add_command(label="Exit", command=self.destroy)


		self.window.config(menu=self.menubar)
		self.window.mainloop()

	def create_rotors(self):
		pass

	def create_plugboard(self):
		pass

	def create_reflector(self):
		pass

	def destroy(self):
		self.window.destroy()