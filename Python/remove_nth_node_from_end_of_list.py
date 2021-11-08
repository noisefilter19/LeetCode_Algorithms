class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = head
        for i in range(n): # Move first n steps to the right
            first = first.next
        if not first: # n == size of list, remove head
            return head.next
        
        second = head
        prev = head
        while first is not None:
            first = first.next
            prev = second
            second = second.next
        # first and second were n nodes apart, so second is n-th from the end
        # Remove "second"
        prev.next = second.next
        return head
