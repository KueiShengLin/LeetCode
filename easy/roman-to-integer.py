class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
                      "IV": 4, "IX": 9, "XL":40, "XC":90, "CD": 400, "CM": 900}
        
        res = 0
        last_roman = 0
        for sid, roman in enumerate(s[::-1]):
            if roman_dict[roman] >= last_roman:
                res += roman_dict[roman]
            else:
                res -= roman_dict[roman]
            
            last_roman = roman_dict[roman]
            
        return res
                