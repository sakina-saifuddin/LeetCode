# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        prev=None
        pali=[]
        curr=head
        arr=[]

        while curr:
            arr.append(curr.val)
            curr=curr.next

        # arr.append(prev)

        print("head", pali)
        print("reverse", arr)

        if arr==arr[::-1]:
            return True
        else:
            return False


        