# LeetCode link: https://leetcode.com/problems/swap-nodes-in-pairs/
# Issue: https://github.com/noisefilter19/LeetCode_Algorithms/issues/736
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        curr = head
        if not head:
            return head
        if not curr.next:
            return curr
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next
        ar1 = [arr[i] for i in range(len(arr)) if i % 2 == 0]
        ar2 = [arr[i] for i in range(len(arr)) if i % 2 != 0]
        full_ar = []
        i = 0
        k = 0
        m = 0
        while m < len(ar1) + len(ar2):
            if i < len(ar2):
                full_ar.append(ar2[i])
                i += 1
            if k < len(ar1):
                full_ar.append(ar1[k])
                k += 1
            m += 1
        head = full_ar[0]
        curr = head
        for i in full_ar:
            curr.next = i
            curr = curr.next
        curr.next = None
        return head
