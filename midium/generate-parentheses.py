class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(sub_set, left, right):
            if len(sub_set)  == 2 * n:
                res.append(sub_set)
                return
            
            if left < n:
                backtracking(sub_set + '(', left+1, right)
            if right < left:
                backtracking(sub_set + ')', left, right+1)
        
        backtracking("", 0, 0)
        return res