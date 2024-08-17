import sys
from turtledemo.chaos import jumpto

from Parser import Parser
from Code import Code

A_INSTRUCTION = 'A_INSTRUCTION'
C_INSTRUCTION = 'C_INSTRUCTION'
L_INSTRUCTION = 'L_INSTRUCTION'

def convert_to_binary(symbol) -> str:
    decimal_integer = int(symbol)
    binary_string = str(bin(decimal_integer))[2:].zfill(16)
    return binary_string

def a_instruction_handler() -> str:
    address = parser.symbol()
    binary_symbol = convert_to_binary(address)
    return binary_symbol

def c_instruction_handler() -> str:
    binary_string = '111'
    dest = code.dest(parser.dest())
    comp = code.comp(parser.comp())
    jump = code.jump(parser.jump())

    binary_string += comp

    if dest == '':
        binary_string += '000'
    else:
        binary_string += dest

    if jump == '':
        binary_string += '000'
    else:
        binary_string += jump

    return binary_string


if __name__ == '__main__':
    filename = sys.argv[1]
    read_path = f"asm/{filename}"
    write_path = f"prog/{filename.split('.')[0]}.hack"

    parser = Parser(read_path)
    code = Code()

    with open(write_path, 'w') as f:

        while parser.has_more_lines():
            parser.advance()
            instruction_type = parser.instruction_type()
            if instruction_type == A_INSTRUCTION:
                f.write(a_instruction_handler()+'\n')
            elif instruction_type == C_INSTRUCTION:
                f.write(c_instruction_handler()+'\n')