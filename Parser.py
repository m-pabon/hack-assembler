import sys

A_INSTRUCTION = 'A_INSTRUCTION'
C_INSTRUCTION = 'C_INSTRUCTION'
L_INSTRUCTION = 'L_INSTRUCTION'

def is_valid_line(s) -> bool:
    if s[0:2] == '//':
        return False
    elif s == '':
        return False
    else:
        return True


class Parser:
    def __init__(self, file_path):
        try:
            f = open(file_path, "r")
            self.file = f.readlines()
            self.current_instruction = ''
        except Exception as e:
            print("Error reading file: ", e)
            sys.exit(1)

    def print_file(self):
        print(self.file)

    def has_more_lines(self):
        return len(self.file) != 0

    def advance(self) -> str:
        if not self.has_more_lines():
            self.current_instruction = ''
            return self.current_instruction

        self.current_instruction = self.file.pop(0).strip()
        if not is_valid_line(self.current_instruction):
            self.current_instruction = self.advance()

        return self.current_instruction

    def instruction_type(self) -> str:
        if self.current_instruction[0] == '@':
            return A_INSTRUCTION
        elif self.current_instruction[0] == '(':
            return L_INSTRUCTION
        else:
            return C_INSTRUCTION

    def symbol(self) -> str:
        instruction_type = self.instruction_type()

        if instruction_type == A_INSTRUCTION:
            return self.current_instruction[1:]
        else:
            return self.current_instruction[1:len(self.current_instruction)-1]

    def dest(self):
        if '=' not in self.current_instruction:
            return ''
        split_instruction = self.current_instruction.split('=')
        return split_instruction[0]

    def comp(self):
        if '=' not in self.current_instruction:
            split_instruction = self.current_instruction.split(';')
            return split_instruction[0]
        elif ';' not in self.current_instruction:
            split_instruction = self.current_instruction.split('=')
            return split_instruction[1]
        else:
            split_instruction = self.current_instruction.split(';')
            second_split = split_instruction[0].split('=')
            return second_split[1]

    def jump(self):
        if ';' not in self.current_instruction:
            return ''
        split_instruction = self.current_instruction.split(';')
        return split_instruction[1]
