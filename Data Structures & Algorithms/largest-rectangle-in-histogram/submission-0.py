class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        # Monotonic stack storing tuples of (start_index, height).
        # Ensures heights in the stack are strictly increasing.
        stack = []

        for i, h in enumerate(heights):
            start = i
            # If current bar is shorter than top of stack, pop stack elements.
            # Pop indicates popped bar can no longer extend further right.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate area with popped bar as height; 
                # width extends to current index i.
                maxArea = max(maxArea, height * (i - index))
                # Push back start index of current height to 
                # left-most popped position.
                start = index
            stack.append((start, h))

        # Calculate max area for remaining bars that 
        # weren't cut off by shorter bar (see example diagram)
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea