class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        now_count = 0
        for c in s[::-1]:
            if c == ' ':
                if now_count != 0:
                    return now_count
            else:
                now_count += 1
                
        return now_count