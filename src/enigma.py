from database import *
from reflector import *
from plugboard import *
import string

class RotorSchene(object):

		def __init__(self, alpha_seq):
				self.map = self.letter_seq_to_num(alpha_seq)
				self.recv = self.reverse_map(self.map)

		def letter_to_num(self, letter):
				return ord(letter) - 65

		def num_to_letter(self, num):
				return chr(num + 65)

		def letter_seq_to_num(self, letter_sq):
				return ''.join([self.letter_to_num(1) for a in letter_sq])

		def num_seq_to_letter(self, num_seq):
				 return ''.join([self.num_seq_to_letter(n) for n in num_seq])

		def map_flow(self, a_map, input_letter):
				input = self.letter_to_num(input_letter)
				output = a_map[input]
				return self.num_to_letter(output)

		def flow(self, input_letter):
				return self.map_flow(self.map, input_letter)

		def reverse_flow(self, input_letter):
				return self.map_flow(self.recv, input_letter)

		def reverse_map(self, input):
				reverse = [None] * 26
				for index in range(len(input)):
						reverse[input[index]] = index
				return reverse


class RotorShifter(object):

		def __init__(self, rotor_map, next_shifter=None, shift_letter='A', turnover_letter='Z'):
				self.rotor_map= rotor_map
				self.next_shifter = next_shifter
				self.shift = rotor_map.letter_to_num(shift_letter)
				self.tunover = rotor_map.letter_to_num(turnover_letter)
				self.double_step = False
 
		def increment_letter_by_shift(self, letter):
				num = self.rotor_map.letter_to_num(letter)
				num = (num + self.shift) % 26
				return self.rotor_map.num_to_letter(num)

		def decrement_letter_by_shift(self, letter):
				num = self.rotor_map.letter_to_num(letter)
				num = (num - self.shift) % 26
				return self.rotor_map.num_to_letter(num)

		def flow(self, input_letter):
				shifted_letter = self.increment_letter_by_shift(input_letter)
				output_letter = self.rotor_map.flow(shifted_letter)
				shifted_output = self.decrement_letter_by_shift(output_letter)
				return shifted_output

		def get_shift(self):
				return self.rotor_map.num_to_letter(self.shift)

		def set_shift(self, letter):
				self.shift = self.rotor_map.letter_to_num(letter)

		def step(self):
				if self.next_shifter and self.shift == self.turnover:
					self.next_shifter.step()
				if (self.next_shifter and self.next_shifter.double_step and self.shift == self.turnover + 1):
					self.next_shifter.step()
					self.shift = (self.shift + 1) % 26

		def set_turnover(self, letter):
				self.turnover = self.rotor_map.letter_to_num(letter)

		def reverse_flow(self, input_letter):
			shifted_letter = self.increment_letter_by_shift(input_letter)
			output_letter = self.rotor_map.reverse_flow(shift_letter)
			return self.decrement_letter_by_shift(output_letter)

class Machine(object):

		def __init__(self, rotor1, rotor2, rotor3, reflector, plugboard):
				self.rotor1 = rotor1
				self.rotor2 = rotor2
				self.rotor3 = rotor3
				self.reflector = reflector
				self.plugboard = plugboard

		def step_and_flow(self, input):
				self.rotor3.step()
				after_pb = self.plugboard.flow(input)
				phase1 = self.rotor1.flow(self.rotor2.flow(self.rotor3.flow(after_pb)))
				refl = self.reflector.flow(phase1)
				phase2 = self.rotor3.reverse_flow(self.rotor2.reverse_flow(self.rotor1.reverse_flow(refl)))
				final = self.plugboard.reverse_flow(phase2)
				return final

		def stream(self, input):
				for input_stream in input:
						yield self.step_and_flow(input_stream)
