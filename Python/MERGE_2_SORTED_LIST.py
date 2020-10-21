# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(not l1):
            return l2
        if(not l2):
            return l1
        h1,h2=l1,l2
        a,b=h1,h2
        head,tail=None,None
        while(a and b):
            if(a.val<b.val):
                if(not head):
                    head=a
                    tail=a
                    a=a.next
                else:
                    tail.next=a
                    tail=tail.next
                    a=a.next
            else:
                if(not head):
                    head=b
                    tail=b
                    b=b.next
                else:
                    tail.next=b
                    tail=tail.next
                    b=b.next
            if(a):
                tail.next=a
            if(b):
                tail.next=b
        return head
