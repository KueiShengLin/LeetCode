class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def bt(now, remain):
            for n in remain:
                new = now + [n]

                if len(new) == len(nums):
                    res.append(new)
                    # return new
                else:
                    now_remain = remain.copy()
                    now_remain.remove(n)
                    bt(new, now_remain)
        
        if len(nums) == 0:
            return [[]]
        
        res = []
        bt([], nums)
        return res