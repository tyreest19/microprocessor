class Processor(object):
    program_counter = 0

    def __init__(self):
        pass

    def print_out_instruction_info(self,instruction):
        print("-----------------------------------------")
        self.program_counter +=1
        print("program counter:", self.program_counter)
        print("OP Code:", instruction.instruction["Opcode"])
        print("RS:", instruction.instruction["RS"])
        print("RT:", instruction.instruction["RT"])
        if instruction.instruction["Opcode"] == 0:
            print("RD:", instruction.instruction["RD"])
            print("Shift Amount:",instruction.instruction["Shift"])
            print("Function Code:",instruction.instruction["FuncCode"])
        else:
            print("Immediate:",instruction.instruction["Immed"])





























