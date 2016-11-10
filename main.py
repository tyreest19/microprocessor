from Decoder import Decoder

def fetch(instructions_file):
    for instructions in instructions_file:
        binary_string = ""
        for bits in instructions:
            if bits != "\n":
                binary_string += bits
        decoder = Decoder(binary_string)
        print(decoder.instruction)
def main():
    instruction_file = open("instruction_list.txt",'r')
    fetch(instruction_file)

if  __name__ == '__main__':
    main()











