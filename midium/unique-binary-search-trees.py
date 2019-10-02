class Solution:
    def numTrees(self, n: int) -> int:
        def compute_bst(bn, now_know):
            bst_n = 0
            # all possible sorting
            # ex: n = 3: left 2 * right 0 + left 1 * right 1 + left 0 * right 2
            for i in range(bn):
                # split left tree and right tree
                l = i
                r = bn-i-1
                # if sub tree is not computed before, compute it
                if now_know[l] == 0:
                    now_know[l] = compute_bst(l, now_know)
                elif now_know[r] == 0:
                    now_know[r] = compute_bst(r, now_know)
                # all possiblie sorting = amount of left * amount right
                bst_n += now_know[l] * now_know[r]
            
            return bst_n
        
        
        know = [0] * (n+1)
        know[0], know[1] = 1, 1
        return compute_bst(n, know)