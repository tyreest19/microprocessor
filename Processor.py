from utils import twos_comp
from utils import convert_int_binary
from  utils import convert_binary_to_hexdicamal
from utils import convert_hexdicamal_to_binary


class Processor(object):
    intial_value = '00000000'

    program_counter = 0
    register_files = {}
    memory_location = {}
    for i in range(33):
        register_files[i] = intial_value
    for i in range(129):
        memory_location[i] = intial_value

    instruction = ""

    def __init__(self):
        pass

    def start_processor(self):
        if self.instruction.instruction["Opcode"] == 0:
            self.decide_r_type_operation()
        else:
            self.decide_i_type_operation()

        print("register files: ",end="")
        for i in range(33):
            print("{0}:{1}".format(i, self.register_files[i]),end="|")
        print()
        print("memory locations: ",end="")
        for i in range(129):
            print("{0}:{1}".format(i, self.memory_location[i]), end="|")
        print()
        print('---------------------------------------------------')


    def set_instruction(self, desired_instruction):
        self.instruction = desired_instruction

    def get_instruction(self):
        return self.instruction

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
        if self.instruction.instruction["FuncCode"] == 42:
            self.slt_operation()

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
        print('Add ${0},${1},${2}'.format(self.instruction.instruction['RD'],
                                          self.instruction.instruction['RS'],
                                          self.instruction.instruction['RT']))
        self.program_counter += 1
        print("program counter:", self.program_counter)
        print("Opcode:",self.instruction.instruction['Opcode'])
        print("RD:",self.instruction.instruction['RD'])
        print("RS:",self.instruction.instruction['RS'])
        print("RT:",self.instruction.instruction['RT'])
        print("Shift Amount:",self.instruction.instruction['Shift'])
        print("FuncCode: ", self.instruction.instruction['FuncCode'])
        rs = self.register_files[self.instruction.instruction['RS']]
        rt = self.register_files[self.instruction.instruction['RT']]
        rs = convert_hexdicamal_to_binary(rs,8)
        rt = convert_hexdicamal_to_binary(rt,8)
        result = int(rs,2) + int(rt,2)
        result = convert_int_binary(result,32)
        result = convert_binary_to_hexdicamal(result)
        self.register_files[self.instruction.instruction['RD']] = result

    def sub_operation(self):
        print('Sub ${0},${1},${2}'.format(self.instruction.instruction['RD'],
                                          self.instruction.instruction['RS'],
                                          self.instruction.instruction['RT']))
        self.program_counter += 1
        print("program counter:", self.program_counter)
        print("Opcode:", self.instruction.instruction['Opcode'])
        print("RD:", self.instruction.instruction['RD'])
        print("RS:", self.instruction.instruction['RS'])
        print("RT:", self.instruction.instruction['RT'])
        print("Shift Amount:", self.instruction.instruction['Shift'])
        print("FuncCode: ", self.instruction.instruction['FuncCode'])
        rs = self.register_files[self.instruction.instruction['RS']]
        rt = self.register_files[self.instruction.instruction['RT']]
        rs = convert_hexdicamal_to_binary(rs,8)
        rt = convert_hexdicamal_to_binary(rt,8)
        rt = twos_comp(rt,True)
        result = int(rs,2) + int(rt,2)
        result = convert_int_binary(result,32)
        result = convert_binary_to_hexdicamal(result)
        self.register_files[self.instruction.instruction['RD']] = result



    def or_operation(self):
        print('OR ${0},${1},${2}'.format(self.instruction.instruction['RD'],
                                          self.instruction.instruction['RS'],
                                          self.instruction.instruction['RT']))
        rs = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RS']], 8)
        rt = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RT']], 8)
        self.program_counter += 1
        print("program counter:", self.program_counter)
        print("Opcode:", self.instruction.instruction['Opcode'])
        print("RD:", self.instruction.instruction['RD'])
        print("RS:", self.instruction.instruction['RS'])
        print("RT:", self.instruction.instruction['RT'])
        print("Shift Amount:", self.instruction.instruction['Shift'])
        print("FuncCode: ", self.instruction.instruction['FuncCode'])
        result = ""
        for i in range(32):
            result += str(int(rs[i]) or int(rt[i]))
        result = convert_binary_to_hexdicamal(result)
        self.register_files[self.instruction.instruction['RD']] = result

    def xor_operation(self):
        print('Xor ${0},${1},${2}'.format(self.instruction.instruction['RD'],
                                          self.instruction.instruction['RS'],
                                          self.instruction.instruction['RT']))
        rs = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RS']], 8)
        rt = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RT']], 8)
        self.program_counter += 1
        print("program counter:", self.program_counter)
        print("Opcode:", self.instruction.instruction['Opcode'])
        print("RD:", self.instruction.instruction['RD'])
        print("RS:", self.instruction.instruction['RS'])
        print("RT:", self.instruction.instruction['RT'])
        print("Shift Amount:", self.instruction.instruction['Shift'])
        print("FuncCode: ", self.instruction.instruction['FuncCode'])
        result = ""
        for i in range(32):
            result += str(int(rs[i]) ^ int(rt[i]))
        result = convert_binary_to_hexdicamal(result)
        self.register_files[self.instruction.instruction['RD']] = result

    def and_operation(self):
        print('And ${0},${1},${2}'.format(self.instruction.instruction['RD'],
                                          self.instruction.instruction['RS'],
                                          self.instruction.instruction['RT']))
        rs = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RS']], 8)
        rt = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RT']], 8)
        self.program_counter += 1
        print("program counter:", self.program_counter)
        print("Opcode:", self.instruction.instruction['Opcode'])
        print("RD:", self.instruction.instruction['RD'])
        print("RS:", self.instruction.instruction['RS'])
        print("RT:", self.instruction.instruction['RT'])
        print("Shift Amount:", self.instruction.instruction['Shift'])
        print("FuncCode: ", self.instruction.instruction['FuncCode'])
        result = ""
        for i in range(32):
            result += str(int(rs[i]) and int(rt[i]))
        result = convert_binary_to_hexdicamal(result)
        self.register_files[self.instruction.instruction['RD']] = result

    def beq_operation(self):
        rs = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RS']], 8)
        rs = int(rs, 2)
        rt = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RT']], 8)
        rt = int(rt, 2)
        if rs == rt:
            self.program_counter += self.instruction.instruction['Immed']
        else:
            self.program_counter += 1
        print('beq ${0},${1},{2}'.format(self.instruction.instruction['RT'],
                                             self.instruction.instruction['RS'],
                                             self.instruction.instruction['Immed']))
        print("program counter:", self.program_counter)
        print("Opcode:", self.instruction.instruction['Opcode'])
        print("RT:", self.instruction.instruction['RT'])
        print("RS:", self.instruction.instruction['RS'])
        print("Immed. : ", self.instruction.instruction['Immed'])

    def bne_operation(self):
        rs = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RS']], 8)
        rs = int(rs, 2)
        rt = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RT']], 8)
        rt = int(rt, 2)
        if rs != rt:
            self.program_counter += self.instruction.instruction['Immed']
        else:
            self.program_counter += 1
        print('bne ${0},${1},{2}'.format(self.instruction.instruction['RT'],
                                         self.instruction.instruction['RS'],
                                         self.instruction.instruction['Immed']))
        print("program counter:", self.program_counter)
        print("Opcode:", self.instruction.instruction['Opcode'])
        print("RT:", self.instruction.instruction['RT'])
        print("RS:", self.instruction.instruction['RS'])
        print("Immed. : ", self.instruction.instruction['Immed'])

    def lw_operation(self):
        print('Lw ${0},{1}(${2})'.format(self.instruction.instruction['RT'],
                                          self.instruction.instruction['Immed'],
                                          self.instruction.instruction['RS']))
        self.program_counter += 1
        print("program counter:", self.program_counter)
        print("Opcode:", self.instruction.instruction['Opcode'])
        print("RT:", self.instruction.instruction['RT'])
        print("RS:", self.instruction.instruction['RS'])
        print("Immed. : ", self.instruction.instruction['Immed'])
        rs = self.instruction.instruction['RS']
        rs = convert_hexdicamal_to_binary(self.register_files[rs],8)
        rs = int(rs,2)
        immediate_value = self.instruction.instruction['Immed']
        result = rs + immediate_value
        self.register_files[self.instruction.instruction['RT']] = self.memory_location[result]

    def sw_operation(self):
        print('Sw ${0},{1}(${2})'.format(self.instruction.instruction['RT'],
                                         self.instruction.instruction['Immed'],
                                         self.instruction.instruction['RS']))
        self.program_counter += 1
        print("program counter:", self.program_counter)
        print("Opcode:", self.instruction.instruction['Opcode'])
        print("RT:", self.instruction.instruction['RT'])
        print("RS:", self.instruction.instruction['RS'])
        print("Immed. : ", self.instruction.instruction['Immed'])
        rs = self.instruction.instruction['RS']
        rs = convert_hexdicamal_to_binary(self.register_files[rs],8)
        rs = int(rs,2)
        immediate_value = self.instruction.instruction['Immed']
        result = rs + immediate_value
        self.memory_location[result] = self.register_files[self.instruction.instruction['RT']]

    def addi_operation(self):
        print('Addi ${0},${1},{2}'.format(self.instruction.instruction['RT'],
                                          self.instruction.instruction['RS'],
                                          self.instruction.instruction['Immed']))
        self.program_counter += 1
        print("program counter:", self.program_counter)
        print("Opcode:", self.instruction.instruction['Opcode'])
        print("RT:", self.instruction.instruction['RT'])
        print("RS:", self.instruction.instruction['RS'])
        print("Immed. : ", self.instruction.instruction['Immed'])
        rs = self.instruction.instruction['RS']
        rs = convert_hexdicamal_to_binary(self.register_files[rs],8)
        rs = int(rs,2)
        immediate_value = self.instruction.instruction['Immed']
        result = rs + immediate_value
        if result < 0:
            result = convert_int_binary(result, 32)
            result = twos_comp(result,True)
            result = convert_binary_to_hexdicamal(result)
            self.register_files[self.instruction.instruction['RT']] = result
            return result
        result = convert_int_binary(result,32)
        result = convert_binary_to_hexdicamal(result)
        self.register_files[self.instruction.instruction['RT']] = result
        return result

    def slt_operation(self):
        print('Slt ${0},${1},${2}'.format(self.instruction.instruction['RD'],
                                          self.instruction.instruction['RS'],
                                          self.instruction.instruction['RT']))
        rs = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RS']], 8)
        rt = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RT']], 8)
        self.program_counter += 1
        print("program counter:", self.program_counter)
        print("Opcode:", self.instruction.instruction['Opcode'])
        print("RD:", self.instruction.instruction['RD'])
        print("RS:", self.instruction.instruction['RS'])
        print("RT:", self.instruction.instruction['RT'])
        print("Shift Amount:", self.instruction.instruction['Shift'])
        print("FuncCode: ", self.instruction.instruction['FuncCode'])
        result = ""
        rs = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RS']],8)
        rs = int(rs,2)
        rt = convert_hexdicamal_to_binary(self.register_files[self.instruction.instruction['RT']],8)
        rt = int(rt,2)
        if rs < rt:
            rd = convert_int_binary(str(1),32)
            rd = convert_binary_to_hexdicamal(rd)
            self.register_files[self.instruction.instruction['RD']] = rd
        else:
            rd = convert_int_binary(str(0), 32)
            rd = convert_binary_to_hexdicamal(rd)
            self.register_files[self.instruction.instruction['RD']] = rd




