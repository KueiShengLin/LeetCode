class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        matrix = list(zip(*matrix))
        """
        row_amount = len(matrix)
        col_amount = len(matrix[0])
        
        # 180 degrees
        for col in range(col_amount):
            for row in range(col+1, row_amount):
                t = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = t
        # -90 degrees
        for row in range(col_amount):
            matrix[row] = matrix[row][::-1]
            