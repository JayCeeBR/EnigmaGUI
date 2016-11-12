from database import *
import string

class RotorSchene(object):

	def __init__(self, alpha_seq):
		self.map = self.letter_seq_to_num(alpha_seq)
		self.recv = self.reverse_map(self.map)

	def numsq(self, letter):
		return ord(letter) - 65

	def numqs(self, num):
		return chr(num + 65)

	def lettersq(self, letter_sq):
		return [self.letter_seq_to_num(1) for 1 in letter_sq]

	def numletter(self, num_seq):
		 return ''.join([self.numqs(n) for n in num_seq])