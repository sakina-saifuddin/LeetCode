# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q=deque([(root, 0)])
        maxwidth=0
      
        while q:
            level=len(q) #new level every time
            firstnode, firstindex=q[0] #leftmost node of every level which is always 0 , _ means it cna be anything in this case its a levelth node object

            for _ in range(level): #iterate for every level
                node, index=q.popleft() #extract the leftmost node first from every level

                lastindex=index #initalzing last index and not using index to calculate width is becuase index will be used to calculate left and right index
                if node.left:
                    q.append((node.left, 2*index))
                if node.right:
                    q.append((node.right, 2*index+1))

            width=lastindex-firstindex+1 #calculating width of the entire level after for loop finishes
            maxwidth=max(maxwidth, width)  #calculating max width of the entire tree after for loop finishes

        return maxwidth
 
                

        
        