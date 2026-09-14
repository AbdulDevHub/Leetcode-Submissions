class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Find the height of both subtrees
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # Update diameter if the path through THIS node is the longest seen so far
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return height of this subtree to the parent
            return 1 + max(left_height, right_height)
        
        get_height(root)
        return self.max_diameter


# =====================================================================
# REFERENCE: Why diameter != (tree_height - 1)
# =====================================================================
# The longest path doesn't always go through the main root!
#
# Consider this lopsided tree:
#
#        1 (Main Root)
#       / \
#      2   8
#     / \
#    3   4
#   /     \
#  5       6
# /         \
# 7           9
#
# 1. Path through Main Root (1): 
#    7 -> 5 -> 3 -> 2 -> 1 -> 8  => 5 edges
#
# 2. Path through Subtree Root (2): 
#    7 -> 5 -> 3 -> 2 -> 4 -> 6 -> 9  => 6 edges
#
# Since 6 > 5, Diameter = 6 (the path never touches Node 1).
#
# Formula at every node: path_length = left_height + right_height
# =====================================================================