# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        self.result=0

        def dfs(node, path):

            if not node:
                return 

            path+=str(node.val)

            if not node.left and not node.right:
                self.result+=int(path,2)
                return

            left=dfs(node.left, path)
            right=dfs(node.right, path)


        dfs(root, "")
        return self.result
        