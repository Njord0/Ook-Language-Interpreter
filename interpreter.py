import pathlib
import sys

from tokens import Tokens, TokensType
from cells import Cell, CellsList


class InterpreterException(Exception):
    pass

class OokInterpreter:
    def __init__(self, raw_code):
        self.raw = raw_code.strip()
        self.pos = -2
        self.cell_pos = 0
        self.cells_list = CellsList()

    def run(self):
        """
            A multitask function
        """

        self.code = self.raw.replace("\n", " ")
        self.code = self.code.split(" ")

        if len(self.code) % 2 != 0:
            raise InterpreterException("Error while parsing code...")

        self.cur_token = self.get_next_token()

        while self.pos < len(self.code):
            self.expr()
            self.cur_token = self.get_next_token()


    
    def get_next_token(self):
        self.pos += 2

        if self.pos + 1 >= len(self.code):
            return
        
        tok = Tokens(self.code[self.pos] + " " + self.code[self.pos+1])

        if tok.type ==  TokensType.INVALID:
            raise InterpreterException(f"Invalid token at position : {self.pos}")

        return tok


    def get_prev_token(self):
        self.pos -= 2

        tok = Tokens(self.code[self.pos] + " " + self.code[self.pos+1])

        if tok.type == TokensType.INVALID:
            raise InterpreterException(f"Invalid token at position : {self.pos}")

        return tok


    def expr(self):
        #print(f"DEBUG: {self.cur_token.type} cell[{self.cell_pos}]: {self.cells_list[self.cell_pos]}")

        if self.cur_token.type == TokensType.R_PTR:
            self.cell_pos += 1

        elif self.cur_token.type == TokensType.L_PTR:
            self.cell_pos -= 1

        elif self.cur_token.type == TokensType.INC_CELL:
            try:
                self.cells_list[self.cell_pos].inc()
            except IndexError:
                raise IndexError(f"Can't access at index: {self.cell_pos}")


        elif self.cur_token.type == TokensType.DEC_CELL:
            try:
                self.cells_list[self.cell_pos].dec()
            except IndexError:
                raise IndexError(f"Can't access at index: {self.cell_pos}")


        elif self.cur_token.type == TokensType.P_CHAR:
            print(chr(self.cells_list[self.cell_pos].value), end="")

        elif self.cur_token.type == TokensType.R_CHAR:
            self.cells_list[self.cell_pos].value = int(sys.stdin.read(1))

        elif self.cur_token.type == TokensType.L_BEGIN:
            if self.cells_list[self.cell_pos].value == 0:
                while (tok:=self.get_next_token()).type != TokensType.L_END:
                    continue 

        elif self.cur_token.type == TokensType.L_END:
            if self.cells_list[self.cell_pos].value != 0:
                while (tok:=self.get_prev_token()).type != TokensType.L_BEGIN:
                    continue

        else:
            print(self.cur_token._text)
            raise InterpreterException(f"Unknow exception at position : {self.pos}")


def usage():
    print("Usage:")
    print(f"\tpython {sys.argv[0]} 'script.ook'")

def main():
    path = pathlib.Path(sys.argv[1])

    if not path.is_file():
        if path.is_dir():
            print(f"\"{sys.argv[1]}\" is a directory")

        return
    with open(sys.argv[1], "r") as file:
        content = file.readlines()

        content = "".join(content)

        a = OokInterpreter(content)
        a.run()

        print()

if len(sys.argv[1:]) != 1:
    usage()

else:
    main()
