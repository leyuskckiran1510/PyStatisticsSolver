def code_to_chars(code):
    CSI = "\033["
    return CSI + str(code) + "m"


class AnsiCodes():
    def __init__(self):
        for name in dir(self):
            if not name.startswith("_") and name != "RGB":
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))


class AFore(AnsiCodes):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    RESET = 39
    LIGHTBLACK_EX = 90
    LIGHTRED_EX = 91
    LIGHTGREEN_EX = 92
    LIGHTYELLOW_EX = 93
    LIGHTBLUE_EX = 94
    LIGHTMAGENTA_EX = 95
    LIGHTCYAN_EX = 96
    LIGHTWHITE_EX = 97

    def RGB(self, r=255, g=255, b=255):
        return "\033[38;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"


class ABack(AnsiCodes):
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47
    RESET = 49
    LIGHTBLACK_EX = 100
    LIGHTRED_EX = 101
    LIGHTGREEN_EX = 102
    LIGHTYELLOW_EX = 103
    LIGHTBLUE_EX = 104
    LIGHTMAGENTA_EX = 105
    LIGHTCYAN_EX = 106
    LIGHTWHITE_EX = 107

    def RGB(self, r=255, g=255, b=255):
        return "\033[48;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"


class AStyle(AnsiCodes):
    BRIGHT = 1
    DIM = 2
    NORMAL = 22
    RESET_ALL = 0
    pass


Fore = AFore()
Back = ABack()
Style = AStyle()

while 1:
    for i in range(0,255,10):
        for j in range(0,255,10):
            for k in range(0,255,10):
                print(Fore.RGB(i,j,k)+Style.BRIGHT+"hello"+Style.RESET_ALL,end="")
            print("\r",end="")
        #print("\n",end="")
