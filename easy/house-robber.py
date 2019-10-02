class Solution:
    def rob(self, nums: List[int]) -> int:
        max_p = 0
        for hid, hp in enumerate(nums):
            if hid <= 1:
                if max_p < hp:
                    max_p = hp
                continue
            elif hid == 2:
                nums[hid] = nums[hid-2] + hp
            else:
                nums[hid] = max(nums[hid-2] + hp, nums[hid-3] + hp)
                # print(nums)
                
            if max_p < nums[hid]:
                max_p = nums[hid]
        
        return max_p