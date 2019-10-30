class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        use for loop is faster than while loop
        """
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        carry = False
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                carry = True
            else:
                carry = False
                digits[i] += 1
                break
                
        # i = len(digits) - 1
        # while i >= 0:
        #     if digits[i] == 9:
        #         digits[i] = 0
        #         i -= 1
        #     else:
        #         digits[i] += 1
        #         break
        
        if carry is True:
            return [1] + digits
            
        return digits
            