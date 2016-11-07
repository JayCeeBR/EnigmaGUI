# -*- coding: latin1 -*-
from tkinter import *


class Window(object):

	def __init__(self):
		self.window = Tk()
		self.window.minsize(800,600)
		self.window.maxsize(800,600)
		self.window.title("Enigma")
		self.plugboard = Frame()
		self.plugboard.pack(side=TOP)

		self.label1 = Label(self.plugboard, text="Plugboard")
		self.label1.pack(side=LEFT)

		self.window.mainloop()

	def destroy(self):
		self.window.destroy()