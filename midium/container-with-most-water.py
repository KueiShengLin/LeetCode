class Solution(object):
    def maxArea(self, height):
        """
        two pointer O(n)
        :type height: List[int]
        :rtype: int
        """
        return_value, left, right = 0, 0, (len(height) - 1)
        while left != right:
            min_h = min(height[left], height[right])
            # print(left, right, min_h, min_h * (right - left))
            if min_h * (right - left) > return_value:
                return_value = min_h * (right - left)
                
            if min_h == height[left]:
                left += 1
            else:
                right -=1

        
        # Brute froce
        # return_value = 0
        # for hid, h in enumerate(height):
        #     if h * (len(height) - hid) < return_value:
        #         continue
        #     for width, h2 in enumerate(height[hid:]):
        #         return_value = max(min(h, h2) * width, return_value)
        return return_value