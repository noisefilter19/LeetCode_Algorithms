"""
Topics: | Linked List |
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # Iterative method
    def swapPairs(self, head):
        """
        Time:  O(n)
        Space: O(1)
        """
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = first.next
            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
            head = head.next

        return dummy.next


#     # Recursive method
#     def swapPairs(self, head):
#         """
#         Time:  O(n)
#         Space: O(n)
#         """
#         if not head or not head.next:
#             return head

#         first = head
#         second = first.next
#         rest = second.next
#         second.next = first
#         first.next = self.swapPairs(rest)
#         return second
