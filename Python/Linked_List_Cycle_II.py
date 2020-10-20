#LeetCode problem link: https://leetcode.com/problems/linked-list-cycle-ii/


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node = head
        val_holder = []
        while(node.next is not None):
            temp = node.val
            val_holder.append(temp)
            if  node.next.val not in val_holder:
                node = node.next
            else:
                return node.next
