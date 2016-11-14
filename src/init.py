# -*- coding: latin1 -*-
from window import *
from database import *
from security import *

class Init(object):

	def __init__(self):
		Security().load_settings()
		Database()
		Window()

	def main(self):
		self.__init__()

if __name__ == "__main__":
	run = Init()