package main

func reverseKGroup(head *ListNode, k int) *ListNode {
	if (head == nil || k == 1 ) {
		return head
	}

	length := 0
	node := head
	for node != nil {
		length++
		node = node.Next
	}

	dummy := ListNode{0, head}
	pre := &dummy

	for step := 0; step + k <= length; step = step + k {
		tail := pre.Next
		next := tail.Next
		for i := 1; i < k; i++ {
			tail.Next = next.Next
			next.Next = pre.Next
			pre.Next = next

			next = tail.Next
		}
		pre = tail
	}


	return dummy.Next
}