"""
Topics: | Linked List | Two Pointers |
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def removeNthFromEnd(self, head, n):
        """
        Time:  O(m)  [m = list length]
        Space: O(1)
        """
        ahead = head
        for _ in range(n):
            ahead = ahead.next
        
        if not ahead:
            return head.next
        
        behind = head
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        behind.next = behind.next.next
        return head