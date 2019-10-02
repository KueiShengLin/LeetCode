class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:       
        now_max, now_max_t = 0, 0
        char_locate = {}
        changed_flag = ""
        if s:
            changed_flag = s[0]
            char_locate[s[0]] = 0
            
        for idx, c in enumerate(s):
            old_c_locate = -1
            if c in char_locate:
                old_c_locate = char_locate[c]
                
            if c == changed_flag:
                char_locate[c] = idx
                tuple_list = [(value,key) for key,value in char_locate.items()]
                min_idx, changed_flag = min(tuple_list)
                now_max_t = idx - min_idx            
            else:
                char_locate[c] = idx
                
            if old_c_locate > char_locate[changed_flag]:
                tuple_list = [(value,key) for key,value in char_locate.items() if value > old_c_locate]
                min_idx, changed_flag = min(tuple_list)
                now_max_t = idx - min_idx
                
            now_max_t += 1
            if now_max_t > now_max:
                now_max = now_max_t
        return now_max