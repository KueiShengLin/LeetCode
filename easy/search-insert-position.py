class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
		if target in nums:
            return nums.index(target)
        
        for nid, n in enumerate(nums):
            if n > target or n == target:
                return nid
            
        return len(nums)
		
        # if len(nums) == 0 or target < nums[0]:
        #     return 0
        #  Binary search
        # split = int(len(nums) / 2)
        # res = 0
        # 
        # while True:
        #     split = int(len(nums) / 2)
        #     print(nums, split, res)
        #     if nums == []:
        #        return res
        #     else:
        #         if nums[split] == target:
        #             return res+split
        #         elif nums[split] > target:
        #             nums = nums[:split]
        #         elif nums[split] < target:
        #             nums = nums[split+1:]
        #             res += split + 1
        #         else:
        #             break
        #         
        # return res+1