class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_elements = n * n
        
        # Create a frequency array for numbers 1 to n^2
        # Index 0 will be left unused for easy 1-to-1 mapping
        counts = [0] * (total_elements + 1)
        
        # Count occurrences of each number
        for row in grid: 
            for num in row: counts[num] += 1
                
        repeated = 0
        missing = 0
        for i in range(1, total_elements + 1):
            if counts[i] == 2: repeated = i
            elif counts[i] == 0: missing = i
            if repeated and missing: break
        return [repeated, missing]
