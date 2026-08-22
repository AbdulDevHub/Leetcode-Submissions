class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            midIndex = (left + right) // 2

            row = midIndex // cols
            col = midIndex % cols
            midValue = matrix[row][col]

            if target == midValue: return True
            elif target > midValue: left = midIndex + 1
            else: right = midIndex - 1
        return False
