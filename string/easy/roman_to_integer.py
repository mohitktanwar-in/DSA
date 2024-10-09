class Solution:
    def romanToInt(self, s: str) -> int:
        rom_to_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        val = 0
        for i in range(len(s)-1,-1,-1):
            if i != (len(s)-1) and rom_to_int[s[i]] >= rom_to_int[s[i+1]]:
                val+=rom_to_int[s[i]]
            elif i != (len(s)-1) and rom_to_int[s[i]] < rom_to_int[s[i+1]]:
                val-=rom_to_int[s[i]]
            else:
                val+=rom_to_int[s[i]]
        
        return val
        #fastest way
        # translations = {
        #     "I": 1,
        #     "V": 5,
        #     "X": 10,
        #     "L": 50,
        #     "C": 100,
        #     "D": 500,
        #     "M": 1000
        # }
        # number = 0
        # s = s.replace("IV", "IIII").replace("IX", "VIIII")
        # s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        # s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        # for char in s:
        #     number += translations[char]
        # return number