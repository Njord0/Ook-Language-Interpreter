import enum

class TokensType(enum.Enum):
    R_PTR = "Ook. Ook?"
    L_PTR = "Ook? Ook."
    INC_CELL = "Ook. Ook."
    DEC_CELL = "Ook! Ook!"
    P_CHAR = "Ook! Ook." #print char at current cell
    R_CHAR = "Ook. Ook!" #read char to current cell

    L_BEGIN = "Ook! Ook?" # loop begin
    L_END = "Ook? Ook!"

    INVALID = ""


class Tokens:
    def __init__(self, text):
        self._text = text
        try:
            self.type = TokensType(self._text)
        except ValueError:
            self.type = TokensType.INVALID
