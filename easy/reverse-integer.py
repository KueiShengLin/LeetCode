class Solution:
    def reverse(self, x: int) -> int:
        overflow = 2**31
        # if x > overflow or x < -overflow:
        #     return -1
        if x >= 0:
            str_x = int(str(x)[::-1])
        else:
            str_x = -int(str(x)[1:][::-1])
            
        if str_x > overflow or str_x < -overflow:
            return 0
        
        return str_x