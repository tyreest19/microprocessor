from Decoder import Decoder
from Processor import  Processor
def fetch(instructions_file):
    processor = Processor()
    for instructions in instructions_file:
        if not instructions.strip():
            return
        binary_string = ""
        for bits in instructions:
            if bits != "\n":
                binary_string += bits
        decoder = Decoder(binary_string)
        processor.set_instruction(decoder)
        processor.start_processor()
def test_virus():
    processor = Processor()
    processor.add_virus()
    for i in range(129):
        print(processor.memory_location[i])
def main():
    instruction_file = open("instruction_list.txt",'r')
    fetch(instruction_file)




if  __name__ == '__main__':
    main()











