class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums.sort()
        pos = sorted(i for i in nums if i > 0)
        pos_s = set(pos)
        zero = [i for i in nums if i == 0]
        neg = sorted(i for i in nums if i < 0)
        neg_s = set(neg)
        res = set([])
        
        if len(nums) < 3:
            return []
        
        if len(zero) >= 3:
            res.add((0,0,0)) 
        if len(zero) > 0:
            for i in neg_s:
                if -i in pos_s:
                    res.add((i,0,-i))
            
        if pos:
            for iid, i in enumerate(neg):
                for j in neg[iid+1:]:
                    if -(i+j) > pos[-1] or -(i+j) < pos[0]:
                        continue
                    elif -(i + j) in pos_s:
                        res.add((i, j, -(i + j)))
        if neg:
            for iid, i in enumerate(pos):
                for j in pos[iid+1:]:
                    if -(i+j) > neg[-1] or -(i+j) < neg[0]:
                        continue
                    elif -(i + j) in neg_s:
                        res.add((-(i + j), i, j))
        

        return list(res)
        