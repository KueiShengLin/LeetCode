class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            rb_x = int(str(x)[-1::-1])
            # rb_x = int(rb_x)
            if rb_x == x:
                return True
            else:
                return False
        else:
            return False