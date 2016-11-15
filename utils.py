"""Utils file this is a file for helper functions"""

def convert_int_binary(number,number_of_bits):
    """convert number int to a desired binary string bit binary string"""
    size_of_bits = '{0:0' + str(number_of_bits) + 'b}'
    binary = size_of_bits.format(int(number))
    return binary

def convert_binary_to_hexdicamal(binary):
    """Convert 32 bit string into 8 bit hexidecimal"""
    hexdecimal = ""
    hexdecimal_chars = {'A': '1010', 'B': '1011',
                        'C': '1100', 'D': '1101', 'E': '1110',
                        'F': '1111'}
    for i in range(0,32,4):
        if int(binary[i:i + 4],2) == 10:
            hexdecimal += "A"
        elif int(binary[i:i + 4], 2) == 11:
            hexdecimal += "B"
        elif int(binary[i:i + 4], 2) == 12:
            hexdecimal += "C"
        elif int(binary[i:i + 4], 2) == 13:
            hexdecimal += "D"
        elif int(binary[i:i + 4], 2) == 14:
            hexdecimal += "E"
        elif int(binary[i:i + 4], 2) == 15:
            hexdecimal += "F"
        else:
            hexdecimal += str(int(binary[i:i + 4],2))
    return hexdecimal

def convert_hexdicamal_to_binary(hexdecimal,size_of_hexdecimal):
    """Convert hexdecimal to binary"""
    binary = ""
    hexdecimal_chars = {'A': '1010', 'B': '1011',
                        'C': '1100', 'D': '1101', 'E': '1110',
                        'F': '1111'}
    for i in range(size_of_hexdecimal):
        if hexdecimal[i] in ("A","B","C","D","E","F"):
            binary += hexdecimal_chars[hexdecimal[i]]
        else:
            binary +=  convert_int_binary(int(hexdecimal[i]),4)
    return binary

def twos_comp(binary,negative_number=False):
    """compute the 2's compliment of int value val"""
    binary = list(binary)
    if int(''.join(binary),2) == 0:
        return '{0:032b}'.format(int('0'))
    elif binary[0] == '1' or negative_number == True:
        for i in range(len(binary)):
            if binary[i] == '1':
                binary[i] = '0'
            else:
                binary[i] = '1'
        binary = ''.join(binary)
        binary = bin(int(binary,2) + 1)
        binary = binary[2:]
    return ''.join(binary)



