# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        def divide(node):
            if not node or not node.next:
                return  node
            dummy=node
            slow=dummy
            fast=dummy

            prev=None

            while fast and fast.next:
                prev=slow
                slow=slow.next
                fast=fast.next.next

            prev.next=None

            leftnode=divide(node)
            rightnode=divide(slow)

            return merge(leftnode, rightnode)

        def merge(left, right):

            dummy=ListNode(0)
            curr=dummy
            
            while left and right:
                if left.val<=right.val:
                    curr.next=left
                    left=left.next
                else:
                    curr.next=right
                    right=right.next
                curr=curr.next

            if right:
                curr.next=right
            if left:
                curr.next=left

            return dummy.next

        result=divide(head)
        return result



        