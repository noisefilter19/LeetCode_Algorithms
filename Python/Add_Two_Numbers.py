# Problem Link: https://leetcode.com/problems/add-two-numbers/

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		suml = self.reverse(l1) + self.reverse(l2)
		head = prev = None
		for x in str(suml)[::-1]:
			node = ListNode(x)
			if prev is not None:
				prev.next = node
			prev = node
			if head is None:
				head = prev
		return head
    
	def reverse(self, l: ListNode):
		n = ''
		while l is not None:
			n = n + str(l.val)
			l = l.next
		return(int(n[::-1]))
