class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] < h:
                res[stack.pop()] += 1  # [1]
            if stack: res[stack[-1]] += 1  # [2]
            stack.append(i)
        return res

# ==============================================================================
# FOOTER NOTES
# ==============================================================================
# Approach: Monotonic decreasing stack traversed left-to-right, maintaining
# indices of persons who can potentially see future taller persons.
#
# [1] Shorter precede-and-block count:
#     When a taller person `h` appears, every popped person from the stack can
#     see `h` (incrementing their count), but `h` blocks their view of anyone 
#     further to the right.
#
# [2] Next-taller boundary visibility:
#     If the stack isn't empty, the person remaining on top is taller than `h`.
#     That person can see `h`, but `h` blocks them from seeing anyone shorter 
#     behind `h`.

# https://assets.leetcode.com/uploads/2021/05/29/queue-plane.jpg
