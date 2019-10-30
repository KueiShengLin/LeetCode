class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def bt(now, now_list, now_sum):
            for cand in range(now, len(candidates)):
                temp_sum = now_sum + candidates[cand]
                if temp_sum == target:
                    res.append(now_list + [candidates[cand]])
                elif temp_sum < target:
                    bt(cand, now_list + [candidates[cand]], temp_sum)
                    
        res = []
        bt(0, [], 0)

        return res 