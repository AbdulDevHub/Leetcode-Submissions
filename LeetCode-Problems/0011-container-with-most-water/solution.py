class Solution:
    def maxArea(self, heights: list[int]) -> int:
        maxArea = 0
        leftPointer = 0
        rightPointer = len(heights) - 1
        
        while leftPointer < rightPointer:
            # 1. Grab the heights of the current boundaries
            left_height = heights[leftPointer]
            right_height = heights[rightPointer]
            
            # 2. Calculate the area
            containerWidth = rightPointer - leftPointer
            containerHeight = min(left_height, right_height)
            containerArea = containerWidth * containerHeight
            
            if containerArea > maxArea: maxArea = containerArea
                
            # 3. Fast-forward past any lines that are shorter or equal
            if left_height < right_height:
                while leftPointer < rightPointer and heights[leftPointer] <= left_height:
                    leftPointer += 1
            else:
                while leftPointer < rightPointer and heights[rightPointer] <= right_height:
                    rightPointer -= 1
                    
        return maxArea
