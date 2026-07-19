class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        leftPointer = 0
        rightPointer = len(heights) - 1
        while leftPointer < rightPointer:
            containerHeight = min(heights[leftPointer], heights[rightPointer])
            containerWidth = rightPointer - leftPointer
            containerArea = containerWidth * containerHeight

            maxArea = max(maxArea, containerArea)
            # Move only the pointer that points to the shorter line
            if heights[leftPointer] < heights[rightPointer]: leftPointer += 1
            else: rightPointer -= 1
        return maxArea