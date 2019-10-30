class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        possible_list = []
        # O(m)
        for i in range(len(matrix)):
            if matrix[i]:
                if matrix[i][0] <= target and matrix[i][-1] >= target:
                    possible_list.append(matrix[i])
        # O(mn)
        for l in possible_list:
            for i in l:
                if i == target:
                    return True
                elif i > target:
                    break
        return False
            