# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        node=root

        return [node.val] + self.preorderTraversal(node.left) + self.preorderTraversal(node.right)

        #1. Give me left result
#2. Add myself
#3. Give me right result
        