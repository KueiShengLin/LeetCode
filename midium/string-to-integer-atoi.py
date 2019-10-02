class Solution:
    def myAtoi(self, string: str) -> int:
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        symbol = ['-', '+']
        output = str()
        count = 0
        if string == "" or string in symbol:
            return 0
        
        while string[count] ==' ':
            count += 1
            if count == len(string):
                return 0

        if string[count] in numbers or string[count] in symbol: 
            output += string[count]
            for ch in string[count+1:]:
                if ch not in numbers:
                    if len(output) == 1 and output in symbol:
                        return 0
                    if int(output) > 2**31 - 1:
                        return 2**31 - 1
                    elif int(output) < -2**31:
                        return -2**31
                    else:
                        return int(output)
                else:
                    output += ch
            if int(output) > 2**31 - 1:
                return 2**31 - 1
            elif int(output) < -2**31:
                return -2**31
            else:
                return int(output)

        return 0