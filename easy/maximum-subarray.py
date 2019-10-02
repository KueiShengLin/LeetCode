class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = nums[0]
        now = nums[0]
        for n_id in range(1, len(nums)):
            # check restart or continue which is better
            now = max(now + nums[n_id], nums[n_id])
            if now > global_max:
                global_max = now
        
        return global_max
                