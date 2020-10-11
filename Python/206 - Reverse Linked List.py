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
    def reverseList(self, head):
        """
        Time:  O(n)
        Space: O(1)
        """
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    # Recursive equivalent
    def _reverseListRecursive(self, curr):
        if not curr or not curr.next:
            return curr  # New head node
        head = self._reverseListRecursive(curr.next)
        curr.next.next = curr
        curr.next = None
        return head
