class Code:
    def __init__(self):
        self.j_mappings = {
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111'
        }
        self.c_mappings = {
            '0': '0101010',
            '1': '0111111',
            '-1': '0111010',
            'D': '0001100',
            'A': '0110000',
            '!D': '0001101',
            '!A': '0110001',
            '-D': '0001111',
            '-A': '0110011',
            'D+1': '0011111',
            'A+1': '0110111',
            'D-1': '0001110',
            'A-1': '0110010',
            'D+A': '0000010',
            'D-A': '0010011',
            'A-D': '0000111',
            'D&A': '0000000',
            'D|A': '0010101',
            'M': '1110000',
            '!M': '1110001',
            '-M': '1110011',
            'M+1': '1110111',
            'M-1': '1110010',
            'D+M': '1000010',
            'D-M': '1010011',
            'M-D': '1000111',
            'D&M': '1000000',
            'D|M': '1010101'
        }

    def dest(self, symbol) -> str:
        # M = 001, D = 010, A = 100
        num = 0
        if 'M' in symbol:
            num += 1
        if 'D' in symbol:
            num += 2
        if 'A' in symbol:
            num += 4

        mask = 0x7
        bits = str(bin(num & mask))[2:].zfill(3)
        return bits

    def jump(self, symbol) -> str:
        return self.j_mappings.get(symbol, '000')

    def comp(self, symbol) -> str:
        return self.c_mappings.get(symbol, '0000000')