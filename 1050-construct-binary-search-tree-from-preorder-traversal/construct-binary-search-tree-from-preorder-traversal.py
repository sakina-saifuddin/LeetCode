# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i=0

        def bst(lower, higher):

            if self.i==len(preorder):
                return None

            if not preorder:
                return None
            
            val=preorder[self.i]

            root=TreeNode(val)

            if val<=lower or val>=higher:
                return None
            self.i+=1

            root.left=bst(lower, val)
            root.right=bst(val, higher)

            return root




        return bst(float(-inf), float(inf))
