# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

# The brute-force solution wastes time by repeatedly recomputing subtree heights.
# We fix this by doing one DFS that returns two things at once for every node:

# Is the subtree balanced? (True/False)
#     1) What is its height?
#     2) This way, each subtree is processed only once.

# If at any node the height difference > 1, we mark it as unbalanced and stop worrying about deeper levels.