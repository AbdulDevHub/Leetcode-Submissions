# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current_level = [root]
        depth = 0

        while current_level:
            if depth % 2 == 1:  # [1]
                for i in range(len(current_level) // 2):
                    j = len(current_level) - 1 - i
                    current_level[i].val, current_level[j].val = (
                        current_level[j].val,
                        current_level[i].val,
                    )  # [2]

            next_level = []
            for node in current_level:
                for child in (node.left, node.right):
                    if child:  # [3]
                        next_level.append(child)

            current_level = next_level
            depth += 1

        return root

# ==============================================================================
# FOOTER NOTES
# ==============================================================================
# Approach: Breadth-first traversal, one level at a time. On each odd-depth
# level, reverse the node values by swapping pairs from both ends inward.
#
# [1] Odd Levels Only:
#     The root is depth 0, so depths 1, 3, 5, ... are the levels to reverse.
#     depth % 2 == 1 selects exactly those levels.
#
# [2] Swap Values, Not Nodes:
#     Only the .val fields are swapped. The tree's shape (the .left and .right
#     pointers) stays intact, so the children gathered for the next level are
#     the same as in the original tree. The middle node of an odd-length level
#     is never touched, which is correct since it has no mirror partner.
#
# [3] Skip Missing Children:
#     Trees can have None children. Filtering them here keeps the level list
#     containing only real nodes, so the swap loop never dereferences None.
#     Iterating left before right keeps each level in left-to-right order,
#     which is what the mirror-swap depends on.
