class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        now_best = 1.0e9
        
        for i in range(len(nums)-2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                now = nums[i] + nums[left] + nums[right]
                
                if now < target:
                    while left < right and nums[left] == nums[left+1]:
                            left += 1
                    left += 1
                elif now > target:
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                else:
                    return now
                
                if abs(now - target) < abs(now_best - target):
                    now_best = now
                    
        return now_best