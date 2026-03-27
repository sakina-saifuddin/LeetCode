# Definition for singly-linked list.
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):

    def addTwoNumbers(self, l1, l2):

        l3head = ListNode(0)  # dummy
        currl3 = l3head
        carry = 0

        while l1 is not None or l2 is not None or carry > 0:
            l1val = 0
            l2val = 0

            if l1:
                l1val = l1.val
            else:
                l1val = 0

            if l2:
                l2val = l2.val
            else:
                l2val = 0
            sum_val = l1val + l2val + carry

            if sum_val < 10:
                currl3.next = ListNode(sum_val)
                carry = 0
            else:
                carry = sum_val // 10
                digitkeep = sum_val % 10
                print(digitkeep)
                currl3.next = ListNode(digitkeep)

            currl3 = currl3.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return l3head.next
