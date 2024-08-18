import sys

from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable

A_INSTRUCTION = 'A_INSTRUCTION'
C_INSTRUCTION = 'C_INSTRUCTION'
L_INSTRUCTION = 'L_INSTRUCTION'
RAM_VARIABLE_ADDRESS_SPACE = 16

def convert_to_binary(symbol) -> str:
    decimal_integer = int(symbol)
    binary_string = str(bin(decimal_integer))[2:].zfill(16)
    return binary_string

def a_instruction_handler(parser) -> str:
    global RAM_VARIABLE_ADDRESS_SPACE
    symbol = parser.symbol()
    # Address can be a symbol or a number
    try:
        # Symbol is a number, convert it to binary directly
        value = int(symbol)
        return convert_to_binary(str(value))
    # Exception is thrown if the address is a symbol, first we check if that symbol is in the symbol table
    except ValueError:
        # Symbol is found
        if symbol_table.contains(symbol):
            address = symbol_table.get_address(symbol)
            return convert_to_binary(str(address))
        # Symbol not found
        else:
            # Add symbol to symbol table
            address = RAM_VARIABLE_ADDRESS_SPACE
            symbol_table.add_entry(symbol, address)
            RAM_VARIABLE_ADDRESS_SPACE += 1
            return convert_to_binary(str(address))

def c_instruction_handler(parser) -> str:
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



if __name__ == "__main__":
    filename = sys.argv[1]
    read_path = f"asm/{filename}"
    write_path = f"prog/{filename.split('.')[0]}.hack"
    code = Code()
    symbol_table = SymbolTable()

    # First Pass
    parser_1 = Parser(read_path)
    line_number = 0
    while parser_1.has_more_lines():
        parser_1.advance()
        instruction_type = parser_1.instruction_type()
        if instruction_type == L_INSTRUCTION:
            label = parser_1.symbol()
            print(f'Encountered Symbol: {label}, adding to symbol table at line_number: {line_number}')
            symbol_table.add_entry(label, line_number)
        else:
            line_number += 1

    # Second Pass
    parser_2 = Parser(read_path)
    with open(write_path, 'w') as f:
        while parser_2.has_more_lines():
            parser_2.advance()
            instruction_type = parser_2.instruction_type()
            if instruction_type == A_INSTRUCTION:
                f.write(a_instruction_handler(parser_2)+'\n')
            elif instruction_type == C_INSTRUCTION:
                f.write(c_instruction_handler(parser_2)+'\n')