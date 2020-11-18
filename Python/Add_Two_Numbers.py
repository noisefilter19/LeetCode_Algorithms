class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add_1 = False
        dummy_head = ListNode(0)
        curr = dummy_head
        while (l1 is not None) or (l2 is not None):
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum = 0 if add_1 is False else 1
            sum += (x + y)
            if sum >= 10:
                sum = sum % 10
                add_1 = True
            else:
                add_1 = False
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            curr.next = ListNode(sum)
            curr = curr.next
        if add_1:
            curr.next = ListNode(1)
        return dummy_head.next