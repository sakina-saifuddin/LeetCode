# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        node=root
        if not node:
            return None
        
        saveVal=node.left #saving node.left val before it gets changed by ndoe.right
        node.left=node.right
        node.right=saveVal    # or you cna write like node.left, node.right=node.right, node.left



        
        left=self.invertTree(node.left)
        right=self.invertTree(node.right)


        return node
        