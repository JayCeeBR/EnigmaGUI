from enigma import *

class Plugboard(object):

	def __init__(self, config):
		normal_map = string.ascii_uppercase
		swapped_map = self.swap_seq_of_pairs(normal_map, config)
		RotorSchene.__init__(self, swapped_map)

	def swap_pair(self, input, pair):
		num_map = self.letter_seq_to_num(input)
		first = self.letter_to_num(pair[0])
		second = self.letter_to_num(pair[1])

		num_map[first] = second
		num_map[second] = first
		return self.num_seq_to_letter(num_map)

	def swap_seq_of_pairs(self, input, seq_of_pairs):
		current_map = input
		for pair in seq_of_pairs:
			current_map = self.swap_pair(current_map, pair)
		return current_map