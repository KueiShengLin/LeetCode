class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for nums_id, num in enumerate(nums):
            nums2 = nums[nums_id+1:]
            for nums_id2, num2 in enumerate(nums2):
                if num + num2 == target:
                    ans = [nums_id, nums_id2 + nums_id + 1]
                    return ans