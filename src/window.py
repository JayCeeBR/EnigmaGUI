# -*- coding: latin1 -*-
from tkinter import *
from security import *


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

		self.textin = Text(self.window, width=98, height=34, bd=3)
		self.textin.pack(side=TOP)

		self.toolbox = Frame(self.window)
		self.toolbox.pack(side=BOTTOM)

		self.btnencode = Button(self.toolbox, text="Encode", command=self.encode)
		self.btnencode.pack(side=LEFT, pady=10, padx=10)

		self.window.config(menu=self.menubar)
		self.window.mainloop()

	def encode(self):
		Security().get_machine()

	def create_rotors(self):
		self.winrotor = Tk()
		self.winrotor.minsize(280, 180)
		self.winrotor.resizable(0,0)
		self.winrotor.maxsize(280, 180)
		self.winrotor.title("Configure Rotor")

		self.frame = Frame(self.winrotor)
		self.frame.pack(side=BOTTOM)

		self.topframe = Frame(self.winrotor)
		self.topframe.pack(side=TOP)

		self.labelrotor = Label(self.topframe, text="Rotor 1 ")
		self.labelrotor.pack(side=TOP, pady=3)
		self.idrotor1 = Entry(self.topframe, bd=3, width=10)
		self.idrotor1.pack(side=TOP, padx=6)
		self.labelrotor = Label(self.topframe, text="Rotor 2 ")
		self.labelrotor.pack(side=TOP)
		self.idrotor2 = Entry(self.topframe, bd=3, width=10)
		self.idrotor2.pack(side=TOP, padx=6)
		self.labelrotor = Label(self.topframe, text="Rotor 3 ")
		self.labelrotor.pack(side=TOP)
		self.idrotor3 = Entry(self.topframe, bd=3, width=10)
		self.idrotor3.pack(side=TOP, padx=6)


		self.idrotor1.insert(0, Security().get_rotors(1))
		self.idrotor2.insert(0, Security().get_rotors(2))
		self.idrotor3.insert(0, Security().get_rotors(3))

		self.btnclose = Button(self.frame, text="Close", command=self.destroy_rotor)
		self.btnclose.pack(side=LEFT, pady=5, padx=5)

		self.btnsave = Button(self.frame, text="Save", command=self.savebtn_rotors)
		self.btnsave.pack(side=LEFT, pady=5, padx=5)

		self.winrotor.mainloop()

	def create_plugboard(self):
		self.plugboard = Tk()
		self.plugboard.minsize(280, 180)
		self.plugboard.resizable(0,0)
		self.plugboard.maxsize(280, 180)
		self.plugboard.title("Configure Plugboard")

		self.plugframe = Frame(self.plugboard)
		self.plugframe.pack(side=TOP)

		self.plugframe2 = Frame(self.plugboard)
		self.plugframe2.pack(side=BOTTOM)

		self.labelplug1 = Label(self.plugframe, text="Pair 1")
		self.labelplug1.pack(side=TOP)

		self.plugpair1 = Entry(self.plugframe, bd=3, width=10)
		self.plugpair1.pack(side=TOP, padx=6)
		self.plugpair11 = Entry(self.plugframe, bd=3, width=10)
		self.plugpair11.pack(side=TOP, padx=6)

		self.labelplug2 = Label(self.plugframe, text="Pair 2")
		self.labelplug2.pack(side=TOP)

		self.plugpair2 = Entry(self.plugframe, bd=3, width=10)
		self.plugpair2.pack(side=TOP, padx=6)
		self.plugpair22 = Entry(self.plugframe, bd=3, width=10)
		self.plugpair22.pack(side=TOP, padx=6)

		self.btnclose2 = Button(self.plugframe2, text="Close", command=self.destroy_plugboard)
		self.btnclose2.pack(side=LEFT, pady=5, padx=5)

		self.btnsave2 = Button(self.plugframe2, text="Save", command=self.savebtn_plugboard)
		self.btnsave2.pack(side=LEFT, pady=5, padx=5)

		self.plugpair1.insert(0, Security().get_plugboard(1))
		self.plugpair11.insert(0, Security().get_plugboard(2))
		self.plugpair2.insert(0, Security().get_plugboard(3))
		self.plugpair22.insert(0, Security().get_plugboard(3))

		self.plugboard.mainloop()

	def create_reflector(self):
		self.winreflector = Tk()
		self.winreflector.minsize(280, 100)
		self.winreflector.resizable(0,0)
		self.winreflector.maxsize(280, 100)
		self.winreflector.title("Configure Reflector")

		self.sideframe = Frame(self.winreflector)
		self.sideframe.pack(side=TOP)
		self.toolframe = Frame(self.winreflector)
		self.toolframe.pack(side=BOTTOM)


		self.labelreflec = Label(self.sideframe, text="Reflector")
		self.labelreflec.pack(side=TOP)

		self.reflector = Entry(self.sideframe, bd=3, width=10)
		self.reflector.pack(side=TOP, padx=6)


		self.reflector.insert(0, Security().get_reflector())

		self.btnclose = Button(self.toolframe, text="Close", command=self.destroy_reflector)
		self.btnclose.pack(side=LEFT, pady=5, padx=5)
		self.btnsave = Button(self.toolframe, text="Save", command=self.savebtn_reflector)
		self.btnsave.pack(side=LEFT, pady=5, padx=5)


		self.winreflector.mainloop()

	def destroy_rotor(self):
		self.winrotor.destroy()

	def destroy_plugboard(self):
		self.plugboard.destroy()

	def destroy_reflector(self):
		self.winreflector.destroy()

	def destroy(self):
		self.window.destroy()

	def savebtn_reflector(self):
		Security().save_reflector(self.reflector.get())
		self.destroy_reflector()

	def savebtn_rotors(self):
		Security().save_rotors(self.idrotor1.get(), self.idrotor2.get(), self.idrotor3.get())
		self.destroy_rotor()

	def savebtn_plugboard(self):
		Security().save_plugboard(self.plugpair1.get(), self.plugpair11.get(), self.plugpair2.get(), self.plugpair22.get())
		self.destroy_plugboard()