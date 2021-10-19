// Link: https://leetcode.com/problems/add-two-numbers/
package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	sol := new(ListNode)
	var indexSol *ListNode
	pass1 := false

	for {
		sum := 0
		if l1 != nil || l2 != nil {
			if l1 != nil {
				sum = l1.Val
				l1 = l1.Next
			}
			if l2 != nil {
				sum += l2.Val
				l2 = l2.Next
			}
		} else if !pass1 {
			break
		}

		if pass1 {
			sum++
		}
		if sum > 9 {
			pass1 = true
		} else {
			pass1 = false
		}

		var val = sum % 10
		if indexSol == nil {
			sol.Val = val
			indexSol = sol
		} else {
			indexSol.Next = &ListNode{Val: val}
			indexSol = indexSol.Next
		}
	}

	return sol
}
