class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        now_path_length = [0 for _ in range(len(triangle))]
        for rid, row in enumerate(triangle):
            t = []
            for nid, n in enumerate(row):        
                # first number
                if nid == 0 :
                    t.append(now_path_length[0] + n)
                # midele numbers
                elif 0 < nid < len(row)-1:
                    t.append(min(now_path_length[nid-1], now_path_length[nid]) + n)
                    # now_path_length[nid] = min(now_path_length[nid-1], now_path_length[nid]) + n
                # last number
                elif nid == len(row)-1:
                    # now_path_length[nid] += n
                    t.append(now_path_length[nid-1] + n)

            for nn_id, new_num in enumerate(t):
                now_path_length[nn_id] = new_num
            # print(t, now_path_length)
            
        return min(now_path_length)