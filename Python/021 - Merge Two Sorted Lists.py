"""
Topics: | Linked List |
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def mergeTwoLists(self, list1, list2):
        """
        Time:  O(m + n)
        Space: O(1)

        [m = len(list1), n = len(list2)]
        """
        result = ListNode(None)  # Dummy head for merged list
        curr = result

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return result.next
