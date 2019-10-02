class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid_locate = []
        if (len(nums1) + len(nums2)) % 2 == 1:
            mid_locate = [int(((len(nums1) + len(nums2)) /2))+1]
        else:
            mid_locate = [(len(nums1) + len(nums2))/2, (len(nums1) + len(nums2))/2 +1 ]
 
        flag_1, flag_2, count, now_mid = 0, 0, 0, 0
        while count < mid_locate[0]:
            if flag_1 >= len(nums1):
                now_mid = nums2[flag_2]
                flag_2 += 1
            elif flag_2 >= len(nums2):
                now_mid = nums1[flag_1]
                flag_1 += 1
            elif nums1[flag_1] < nums2[flag_2]:
                now_mid = nums1[flag_1]
                flag_1 += 1
            else:
                now_mid = nums2[flag_2]
                flag_2 += 1
            count += 1

        if len(mid_locate) == 1:
            return now_mid
        else:
            if flag_1 >= len(nums1):
                return ((now_mid + nums2[flag_2]) / 2)
            elif flag_2 >= len(nums2):
                return ((now_mid + nums1[flag_1]) / 2)
            else:
                return ((now_mid + min(nums1[flag_1], nums2[flag_2])) / 2)