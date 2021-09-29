# Problem URL : https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseNextK(self, previous, current, k):

        if (current == None):
            return None, None

        if (k == 1):
            nextNode = current.next
            current.next = previous
            return (current, nextNode)

        newHead, nextHead = self.reverseNextK(current, current.next, k - 1)
        if (newHead == None):
            return (None, None)
        else:
            current.next = previous
            return (newHead, nextHead)

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        newHead, nextHead = self.reverseNextK(None, head, k)

        if (newHead == None):
            return head
        else:
            result = newHead

        previousTail = head

        while (nextHead != None):
            currentNode = nextHead
            newHead, nextHead = self.reverseNextK(None, currentNode, k)
            if (newHead != None):
                previousTail.next = newHead
            else:
                previousTail.next = currentNode
            previousTail = currentNode
        return result
