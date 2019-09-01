class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        # zip(*str): 逐一讀取list element 當作zip element
        for zs in zip(*strs):
            print(zs)
            if len(set(zs)) == 1:
                res += zs[0]
            else:
                break
                
        return res