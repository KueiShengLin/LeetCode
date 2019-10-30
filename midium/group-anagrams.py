class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            key = ""
            for w in sorted(s):
                key += w
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
                
                
        return list(res.values())
    
