# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
   

        def isMirror(left, right):

            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val!=right.val:
                return False

            leftnode=isMirror(left.left, right.right)
            rightnode=isMirror(left.right, right.left)

            return leftnode and rightnode



        if root:
           value=isMirror(root.left, root.right)
           return value
        return True



        
