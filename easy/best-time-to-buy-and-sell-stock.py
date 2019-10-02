class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bs_arr = [1.0e9,0]
        for p in prices:
            # print(bs_arr, p)
            # bs_arr[0] = min(bs_arr[0], p)
            # bs_arr[1] = max(bs_arr[1], p - bs_arr[0])
            if bs_arr[0] > p:
                bs_arr[0] = p
            if bs_arr[1] < p - bs_arr[0]:
                bs_arr[1] = p - bs_arr[0]
                
        return bs_arr[1]