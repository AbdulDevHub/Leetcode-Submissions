class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]: return
            
        ROWS, COLS = len(matrix), len(matrix[0])
        # Create a padded matrix of size (ROWS + 1) x (COLS + 1) filled with 0s.
        # The extra padding handles edge cases (like row1=0 or col1=0) without if-statements.
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # Fill the prefix sum matrix
        for r in range(ROWS):
            for c in range(COLS):
                # Standard 2D prefix sum formula:
                # Current sum = current element + top sum + left sum - diagonal top-left sum (to avoid double counting)
                self.sumMat[r + 1][c + 1] = (
                    matrix[r][c] 
                    + self.sumMat[r][c + 1] 
                    + self.sumMat[r + 1][c] 
                    - self.sumMat[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Shift coordinates by +1 to account for the 1-indexed padding in sumMat
        # Note: We look at (row2 + 1) and (col2 + 1) for the bottom-right boundary
        bottom_right = self.sumMat[row2 + 1][col2 + 1]
        above        = self.sumMat[row1][col2 + 1]
        left         = self.sumMat[row2 + 1][col1]
        top_left     = self.sumMat[row1][col1]
        
        # Inclusion-Exclusion Principle:
        # Start with the total sum from (0,0) to (row2, col2).
        # Subtract the region above and the region to the left.
        # Add back the top-left intersection because it was subtracted twice.
        return bottom_right - above - left + top_left
