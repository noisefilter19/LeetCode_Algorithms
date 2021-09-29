# Problem Link: https://leetcode.com/problems/merge-k-sorted-lists/

from heapq import merge


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = list(filter(lambda x: x is not None, lists))

        array_list = []
        array = []
        for l in lists:
            node = l

            while node:
                array.append(node.val)
                node = node.next

            array_list.append(array)
            array = []

        if (len(array_list) > 0):
            merge_list = array_list[0]

            for i in range(len(array_list) - 1):
                merge_list = list(merge(merge_list, array_list[i + 1]))

            linked_list = output = ListNode(int(merge_list[0]))

            for j in range(len(merge_list) - 1):
                output.next = ListNode(int(merge_list[j + 1]))
                output = output.next

            return linked_list
        else:
            linked_list = output = ListNode(None)
            return output.next