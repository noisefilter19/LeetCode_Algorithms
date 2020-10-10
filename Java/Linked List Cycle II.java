// https://leetcode.com/problems/linked-list-cycle-ii/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode fast=head;
        ListNode slow=head;
        boolean flag=false;
        while(fast!=null && fast.next!=null && slow!=null){
            fast=fast.next.next;
            slow=slow.next;
            if(slow==fast){
                flag=true;
                break;
            }
        }
        if(flag){
            slow=head;
            while(slow!=fast){
                slow=slow.next;
                fast=fast.next;
            }
            return slow;
        }else{
            return null;
        }
    }
}
