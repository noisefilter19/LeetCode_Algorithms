"""
Topics: | Linked List | Math |
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def addTwoNumbers(self, list1, list2):
        """
        Time:  O(max(m, n))
        Space: O(max(m, n))

        [m = len(list1), n = len(list2)]
        """
        sum_list_sentinel = ListNode(None)
        sum_list = sum_list_sentinel

        carry = 0
        while list1 or list2 or carry:
            sum = carry
            if list1:
                sum += list1.val
                list1 = list1.next
            if list2:
                sum += list2.val
                list2 = list2.next

            carry = sum // 10
            sum %= 10

            sum_list.next = ListNode(sum)
            sum_list = sum_list.next

        return sum_list_sentinel.next
