# -*- coding: latin1 -*-
from tkinter import *


class Window(object):

	def __init__(self):
		self.window = Tk()
		self.window.minsize(800,600)
		self.window.maxsize(800,600)
		self.window.title("Enigma")
		self.window.resizable(0,0)

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
		self.winrotor = Tk()
		self.winrotor.minsize(400, 300)
		self.winrotor.resizable(0,0)
		self.winrotor.maxsize(400, 300)
		self.winrotor.title("Configure Rotor")

		self.frame = Frame(self.winrotor)
		self.frame.pack(side=BOTTOM)

		self.btnclose = Button(self.frame, text="Close", command=self.destroy_rotor)
		self.btnclose.pack(side=LEFT, pady=5, padx=5)

		self.btnsave = Button(self.frame, text="Save")
		self.btnsave.pack(side=LEFT, pady=5, padx=5)

		self.winrotor.mainloop()

	def create_plugboard(self):
		pass

	def create_reflector(self):
		pass

	def destroy_rotor(self):
		self.winrotor.destroy()

	def destroy_plugboard(self):
		pass

	def destroy_reflector(self):
		pass

	def destroy(self):
		self.window.destroy()