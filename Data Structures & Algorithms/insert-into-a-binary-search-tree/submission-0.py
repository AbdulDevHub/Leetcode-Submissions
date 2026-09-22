# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)

        node = root
        while True:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                    break
                node = node.right
                
        return root