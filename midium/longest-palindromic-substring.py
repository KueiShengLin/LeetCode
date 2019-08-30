class Solution:
    def longestPalindrome(self, s: str) -> str:
        global_best = ""
        
        #!!!WRONG CODE!!!
        for init_right_key in range(len(s)):
            if len(global_best) >= len(s) - init_right_key:
                break
                
            local_best_right, local_best_left = "", ""
            right_key = init_right_key
            for left_key, left in enumerate(s[::-1]):
                if right_key + left_key + 1 == len(s):
                    local_best_left += left
                    break
                elif s[right_key] != left and local_best_left != "":
                    local_best_right, local_best_left = "", ""
                    right_key = init_right_key
                elif s[right_key] == left:
                    local_best_right += s[right_key]
                    local_best_left += left
                    right_key += 1
                    if right_key + left_key + 1 == len(s):
                        break
            
            local_best = local_best_right + local_best_left[::-1]
            print(local_best_right, local_best_left)
            if len(local_best) > len(global_best):
                global_best = local_best
                
        return global_best