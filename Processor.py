from utils import twos_comp
from utils import convert_int_binary
from  utils import convert_binary_to_hexdicamal
from utils import convert_hexdicamal_to_binary


class Processor(object):
    program_counter = 0
    register_files = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0,
                      15: 0}
    memory_location = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0,
                       15: 0}
    instruction = ""

    def __init__(self):
        pass
    def print_results(self):
        print("register files: ",end="")
        for i in range(16):
            print(i,":",self.register_files[i],end="|")
        print()
        print("memory locations: ",end="")
        for i in range(16):
            print(i, ":", self.memory_location[i], end="|")


    def set_instruction(self, desired_instruction):
        self.instruction = desired_instruction

    def get_instruction(self):
        return self.instruction

    def print_out_instruction_info(self):
        print("-----------------------------------------")
        self.program_counter += 1
        print("program counter:", self.program_counter)
        print("OP Code:", self.instruction.instruction["Opcode"])
        print("RS:", self.instruction.instruction["RS"])
        print("RT:", self.instruction.instruction["RT"])
        if self.instruction.instruction["Opcode"] == 0:
            print("RD:", self.instruction.instruction["RD"])
            print("Shift Amount:", self.instruction.instruction["Shift"])
            print("Function Code:", self.instruction.instruction["FuncCode"])
        else:
            print("Immediate:", self.instruction.instruction["Immed"])

    def decide_r_type_operation(self):
        if self.instruction.instruction["FuncCode"] == 32:
            self.add_operation()
        if self.instruction.instruction["FuncCode"] == 34:
            self.sub_operation()
        if self.instruction.instruction["FuncCode"] == 36:
            self.and_operation()
        if self.instruction.instruction["FuncCode"] == 37:
            self.or_operation()
        if self.instruction.instruction["FuncCode"] == 38:
            self.xor_operation()

    def decide_i_type_operation(self):
        if self.instruction.instruction["Opcode"] == 4:
            self.beq_operation()
        if self.instruction.instruction["Opcode"] == 5:
            self.bne_operation()
        if self.instruction.instruction["Opcode"] == 8:
            self.addi_operation()
        if self.instruction.instruction["Opcode"] == 35:
            self.lw_operation()
        if self.instruction.instruction["Opcode"] == 43:
            self.sw_operation()

    def add_operation(self):
        rs = self.register_files[self.instruction.instruction['RS']]
        rt = self.register_files[self.instruction.instruction['RT']]
        rs = convert_hexdicamal_to_binary(rs,8)
        rt = convert_hexdicamal_to_binary(rt,8)
        result = int(rs,2) + int(rt,2)
        result = convert_int_binary(result,32)
        result = convert_binary_to_hexdicamal(result)
        self.register_files[self.instruction.instruction['RD']] = result

    def sub_operation(self,rs,rt):
        rs = self.register_files[self.instruction.instruction['RS']]
        rt = self.register_files[self.instruction.instruction['RT']]
        rs = convert_hexdicamal_to_binary(rs,8)
        rt = convert_hexdicamal_to_binary(rt,8)
        rt = twos_comp(rt,True)
        result = int(rs,2) + int(rt,2)
        result = convert_int_binary(result,32)
        result = convert_binary_to_hexdicamal(result)
        self.register_files[self.instruction.instruction['RD']] = result
        '''rs = convert_hexdicamal_to_binary(rs,8)
        rt = convert_hexdicamal_to_binary(rt,8)
        rt = twos_comp(rt,True)
        result = int(rs,2)  + int(rt,2)
        result = convert_int_binary(result,32)
        result = convert_binary_to_hexdicamal(result)
        return result'''


    def or_operation(self):
        rs = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RS']], 8)
        rt = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RT']], 8)
        result = ""
        for i in range(32):
            result += str(int(rs[i]) or int(rt[i]))
        result = convert_binary_to_hexdicamal(result)
        self.register_files[self.instruction.instruction['RD']] = result

    def xor_operation(self):
        rs = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RS']], 8)
        rt = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RT']], 8)
        result = ""
        for i in range(32):
            result += str(int(rs[i]) ^ int(rt[i]))
        result = convert_binary_to_hexdicamal(result)
        self.register_files[self.instruction.instruction['RD']] = result

    def and_operation(self):
        rs = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RS']], 8)
        rt = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RT']], 8)
        result = ""
        for i in range(32):
            result += str(int(rs[i]) and int(rt[i]))
        result = convert_binary_to_hexdicamal(result)
        self.register_files[self.instruction.instruction['RD']] = result

    def beq_operation(self):
        if self.instruction.instruction['RS'] == self.instruction.instruction['RT']:
            self.program_counter += self.instruction.instruction['Immed']

    def bne_operation(self):
        if self.instruction.instruction['RS'] != self.instruction.instruction['RT']:
            self.program_counter += self.instruction.instruction['Immed']

    def lw_operation(self):
        rs = self.instruction.instruction['RS']
        rs = convert_hexdicamal_to_binary(self.register_files[rs],8)
        rs = int(rs,2)
        immediate_value = self.instruction.instruction['Immed']
        result = rs + immediate_value
        self.register_files[self.instruction.instruction['RT']] = self.memory_location[result]

    def sw_operation(self):
        rs = self.instruction.instruction['RS']
        rs = convert_hexdicamal_to_binary(self.register_files[rs],8)
        rs = int(rs,2)
        immediate_value = self.instruction.instruction['Immed']
        result = rs + immediate_value
        self.memory_location[result] = self.register_files[self.instruction.instruction['RT']]

    def addi_operation(self):
        rs = self.instruction.instruction['RS']
        rs = convert_hexdicamal_to_binary(self.register_files[rs],8)
        rs = int(rs,2)
        immediate_value = self.instruction.instruction['Immed']
        result = rs + immediate_value
        result = convert_int_binary(result,32)
        result = convert_binary_to_hexdicamal(result)
        self.register_files[self.instruction.instruction['RT']] = result
        return result



