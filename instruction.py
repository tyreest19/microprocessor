class Instruction(object):
	# transforms a hexdecimal string into instruction format
	instruction = dict() # the instruction in instruction format
	binary_instruction_string = str() # the as a binary string
	def __init__(self,inputed_instruction):
		self.instruction_to_binary(inputed_instruction)
		self.decide_instruction_format()
	
	def instruction_to_binary(self,inputed_instruction):
		"""Converts hexdecimal to binary"""
		hexdecimal_chars = {'A':'1010','B':'1011',
			'C':'1100', 'D':'1101','E':'1110',
			'F':'1111'} #dictionary of hexdecimal chars and binary values
		for bit in inputed_instruction:
			print(bit)
			if bit in hexdecimal_chars:
				self.binary_instruction_string += hexdecimal_chars[bit]
			else:
				bit = '{0:04b}'.format(int(bit))
				self.binary_instruction_string += bit

	def decide_instruction_format(self):
		"""Decides instruction format of a instruction """
		print("im in deicde")
		if int(self.binary_instruction_string[0:6],2) == 0:
			self.convert_to_r_format()
		elif int(self.binary_instruction_string[0:6],2) == 2:
			self.convert_to_i_format()
		else: 
			self.convert_to_i_format()

	def convert_to_r_format(self):	
		""" Converts instruction to r-format"""	
		binary = self.binary_instruction_string
		print(binary)
		self.instruction.update({"Opcode":int(binary[0:6],2)})
		self.instruction.update({"RS":int(binary[6:11],2)})
		self.instruction.update({"RT":int(binary[11:16],2)})
		self.instruction.update({"RD":int(binary[16:21],2)})
		self.instruction.update({"Shift":int(binary[21:26],2)})
		self.instruction.update({"FuncCode":int(binary[26:32],2)})

	def convert_to_i_format(self):	
		""" Converts instruction to i-format"""	
		binary = self.binary_instruction_string
		print(binary)
		self.instruction.update({"Opcode":int(binary[0:6],2)})
		self.instruction.update({"RS":int(binary[6:11],2)})
		self.instruction.update({"RT":int(binary[11:16],2)})
		self.instruction.update({"Immed":int(binary[16:32],2)})

	def convert_to_i_format(self):	
		""" Converts instruction to i-format"""	
		binary = self.binary_instruction_string
		print(binary)
		self.instruction.update({"Opcode":int(binary[0:6],2)})
		self.instruction.update({"TargetAddress":int(binary[6:32],2)})


def main():
	get_input = str(input("enter a hexdecimal: "))
	instruction = Instruction(get_input)
	print(instruction.instruction)

if __name__ == '__main__':
	main()