class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l < r:
            mid = int((r + l) / 2)
            if mid * mid < x:
                l = mid + 1
            else:
                r = mid
        
        if l * l > x:
            return l - 1
        return l
        
        
                