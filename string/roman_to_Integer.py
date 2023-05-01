class Solution:
    def __init__(self):
        self.roman_symb_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        self.result = 0

    def check_valid_len(self, s):
        try:
            if len(s):
                if len(s) < 2:
                    return self.roman_symb_val[s]
            else:
                raise
        except (BaseException,):
            message = "translation is impossible, the input value is an empty string"
            BaseException(message)

    def romanToInt(self, s: str) -> int:
        self.check_valid_len(s)
        try:
            symb = 0
            while True:
                if s[symb] in self.roman_symb_val.keys():
                    if symb == len(s) - 1:
                        self.result += self.roman_symb_val[s[symb]]
                        return self.result
                    if self.roman_symb_val[s[symb]] >= self.roman_symb_val[s[symb + 1]]:
                        self.result += self.roman_symb_val[s[symb]]
                        symb += 1
                    else:
                        subtracting = self.roman_symb_val[s[symb + 1]] - self.roman_symb_val[s[symb]]
                        self.result += subtracting
                        if symb + 1 == len(s) - 1:
                            return self.result
                        else:
                            symb += 2
                else:
                    raise
        except (BaseException,):
            message = "the symbol does not correspond to a roman number"
            BaseException(message)