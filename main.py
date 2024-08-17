import sys
from Parser import Parser

A_INSTRUCTION = 'A_INSTRUCTION'
C_INSTRUCTION = 'C_INSTRUCTION'
L_INSTRUCTION = 'L_INSTRUCTION'

if __name__ == '__main__':
    filename = sys.argv[1]
    path = f"asm/{filename}"

    parser = Parser(path)

    while parser.has_more_lines():
        parser.advance()
        instruction_type = parser.instruction_type()
        print(f'{parser.current_instruction}: {parser.instruction_type()}')
        if instruction_type == A_INSTRUCTION or instruction_type == L_INSTRUCTION:
            print(f'Symbol: {parser.symbol()}')
        if instruction_type == C_INSTRUCTION:
            print(f'DEST = {parser.dest()}, COMP = {parser.comp()}, JUMP = {parser.jump()}')
        print()