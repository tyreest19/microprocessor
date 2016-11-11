class Decoder(object):
    # transforms a hexdecimal string into instruction format
    instruction = dict()  # the instruction in instruction format
    binary_instruction_string = str()  # the as a binary string

    def __init__(self, inputed_instruction):
        self.instruction_to_binary(inputed_instruction)
        self.convert_to_instruction_format()

    def instruction_to_binary(self, inputed_instruction):
        """Converts hexdecimal to binary"""
        hexdecimal_chars = {'A': '1010', 'B': '1011',
                            'C': '1100', 'D': '1101', 'E': '1110',
                            'F': '1111'}  # dictionary of hexdecimal chars and binary values
        for bit in inputed_instruction:
            if bit in hexdecimal_chars:
                self.binary_instruction_string += hexdecimal_chars[bit]
            else:
                bit = '{0:04b}'.format(int(bit))
                self.binary_instruction_string += bit

    def convert_to_instruction_format(self):
        """ Converts instruction to r-format"""
        binary = self.binary_instruction_string
        self.instruction.update({"Opcode": int(binary[0:6], 2)})
        self.instruction.update({"RS": int(binary[6:11], 2)})
        self.instruction.update({"RT": int(binary[11:16], 2)})
        self.instruction.update({"RD": int(binary[16:21], 2)})
        self.instruction.update({"Shift": int(binary[21:26], 2)})
        self.instruction.update({"FuncCode": int(binary[26:32], 2)})
        self.instruction.update({"Immed": binary[16:32]})
        self.instruction["Immed"] = self.twos_comp(int(self.instruction["Immed"],2),len(self.instruction["Immed"]))

    def twos_comp(self, value, bits):
        """compute the 2's compliment of int value val"""
        if (value & (1 << (bits - 1))) != 0:  # if sign bit is set e.g., 8bit: 128-255
            value = value - (1 << bits)  # compute negative value
        return value  # return positive value as is


def main():
    get_input = str(input("enter a hexdecimal: "))
    instruction = Decoder(get_input)
    print(instruction.instruction)


if __name__ == '__main__':
    main()
