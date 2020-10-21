# LeetCode link: https://leetcode.com/problems/reorder-list/
# Issue: https://github.com/noisefilter19/LeetCode_Algorithms/issues/522
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        curr = head
        temp_array = []
        while curr:
            temp_array.append(curr)
            curr = curr.next
        left = 0
        right = len(temp_array) - 1
        curr = head
        for _ in range(len(temp_array)):
            if _ % 2 == 0:
                curr.next = temp_array[left]
                left += 1
            else:
                curr.next = temp_array[right]
                right -= 1
            curr = curr.next
            if left > right:
                curr.next = None

