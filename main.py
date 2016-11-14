from Decoder import Decoder
from Processor import  Processor
def fetch(instructions_file):
    processor = Processor()
    for instructions in instructions_file:
        binary_string = ""
        for bits in instructions:
            if bits != "\n":
                binary_string += bits
        decoder = Decoder(binary_string)
        print(decoder.instruction)
        #processor.set_instruction(decoder)
        #processor.print_out_instruction_info()
        #print(processor.sub_operation("ABCDEFAB","FEDCBAFE"))

def main():
    instruction_file = open("instruction_list.txt",'r')
    #fetch(instruction_file)
    processor = Processor()
    print(processor.print_results())

if  __name__ == '__main__':
    main()











