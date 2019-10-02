class Solution:
    def all2all(self, list1: List[str], list2: List[str]) -> List[str]:
            combine_list = []
            for letter1 in list1:
                for letter2 in list2:
                    combine_list.append(letter1 + letter2)
            return combine_list
        
    def letterCombinations(self, digits: str) -> List[str]: 
        if digits == "":
            return []
        
        d2l = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'],
               '0': [], '1': []}
        
        res = d2l[digits[0]]
        
        for number in digits[1:]:
            res = self.all2all(res, d2l[number])
                
        return res
    