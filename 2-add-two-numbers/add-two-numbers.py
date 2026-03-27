# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# # class Solution(object):

    

# #     def addTwoNumbers( self, l1, l2):
# #         print("l1", l1)
# #         print("l2", l2)

        

# #         dummy=ListNode(0)
# #         currl3=dummy
# #         currl1=l1
# #         currl2=l2

# #         # if l3 is None:
# #         #     l3=currl1.val+currl2.val
# #         #     return l3

# #         while currl1 is not None and currl2 is not None:
# #             l3.next=currl1.val+currl2.val
# #             currl1=currl1.next
# #             currl2=currl2.next

# #         return l3
# #         #     if l3 is None:
# #         #         l3=currl1.val+currl2.val


# class Solution(object):

#     def addTwoNumbers(self, l1, l2):

#         dummy = ListNode(0)   # fake head
#         curr = dummy              # pointer to build list

#         while l1 is not None and l2 is not None:
#             sum_val = l1.val + l2.val
            
#             new_node = ListNode(sum_val)  # ✅ create node
            
#             curr.next = new_node   # ✅ attach node
#             curr = curr.next       # ✅ move forward

#             l1 = l1.next
#             l2 = l2.next

#         return dummy.next


# def printList(head):
#     curr=head
#     while curr is not None:
#         print(curr.val, end="->")
#         curr=curr.next
        
        
#     print("None")


# if __name__=="__main__":
#     ListNode1=ListNode(2)
#     ListNode2=ListNode(4)
#     ListNode3=ListNode(3)

#     head1=ListNode1
#     head1.next=ListNode2
#     head1.next.next=ListNode3

#     ListNode4=ListNode(5)
#     ListNode5=ListNode(6)
#     ListNode6=ListNode(4)

#     head2=ListNode4
#     head2.next=ListNode5
#     head2.next.next=ListNode6

#     printList(head1)
#     printList(head2)

#     l3=Solution().addTwoNumbers(head1,head2)



# Definition for singly-linked list.
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):

    def printlist(self, l1):
        curr=l1
        while curr is not None:
            print(curr.val, end="->")
            curr=curr.next
        print("None")
   

    def addTwoNumbers(self, l1, l2):

        self.printlist(l1)
        self.printlist(l2)

        l3head=ListNode(0)
        currl3=l3head
        carry=0

        while l1 is not None or l2 is not None or carry:
            val1 = l1.val if l1 else 0  # use 0 if this list is exhausted
            val2 = l2.val if l2 else 0
            sum_val=val1+val2+carry
            if sum_val < 10:
                carry=0
                
                currl3.next=ListNode(sum_val)
                
                
            else:
              carry=sum_val // 10 #tens carry to next node
              digit=sum_val % 10 #ones put it in the digit
              currl3.next=ListNode(digit)

            currl3=currl3.next
            if l1: l1=l1.next
            if l2: l2=l2.next

        return l3head.next
           
       