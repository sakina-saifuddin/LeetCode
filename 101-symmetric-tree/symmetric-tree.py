# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        q=deque([(root.left, root.right)])

        while q:

            leftnode, rightnode=q.popleft()

            if not leftnode and not rightnode:
                continue

            if not leftnode or not rightnode:
                return False

            if leftnode.val!=rightnode.val:
                return False

            q.append((leftnode.left, rightnode.right))
            q.append((leftnode.right, rightnode.left))

        return True


        





        
        left=self.isSymmetric()
        