class Solution(object):
    def intToRoman(self, num):
        """
        easy if else check
        :type num: int
        :rtype: str
        """
        
        # roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        roman_dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        
        now_digit = 10 ** (len(str(num)) - 1)
        res = ""
        for number in str(num):
            number = int(number)
            # print(now_digit, number)
            if int(number) in [1,2,3]:
                res += (roman_dict[now_digit] * number)
            elif number in [4]:
                res += (roman_dict[now_digit] + roman_dict[now_digit * 5])
            elif number in [5]:
                res += (roman_dict[now_digit * number])
            elif number in [6,7,8]:
                res += (roman_dict[now_digit * 5] + (roman_dict[now_digit] * (number - 5)))
            elif number in [9]:
                res += (roman_dict[now_digit] + roman_dict[now_digit * 10])
                
            now_digit /= 10
        
        return res