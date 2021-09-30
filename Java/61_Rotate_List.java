/*

Problem No: 61  Rotate List
URI: https://leetcode.com/problems/rotate-list/
Logic: Calculate the length of the linked linst and store each node in a seperate arraylist in the first pass and if the value 
of k is less than length then rotation point will be length-k else multiple rotations happends this can be done by the following logic
till length - k > 0 the value of k is updated as k-length. Swap the next pointers for the rotation point and last node of the listarray 
to length-k node and start respectively
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null | k==0){
            return head;
        }
        int length = 0;
        int pivotPoint;
        List<ListNode> store = new ArrayList<>();
        while(true){
            length++;
            store.add(head);
            head=head.next;
            if(head==null){
                break;
            }
        }
        ListNode newHead = head;
        while(k>length){
            k-=length;
        }
        if(length==k){
            return store.get(0);
        }
        newHead = store.get(length-k);
        ListNode curr = newHead;
        while(curr.next!=null){
            curr=curr.next;
        }
        curr.next = store.get(0);
        if(length-k!=0)
            store.get(length-k-1).next=null;
        else
            store.get(store.size()-1).next=null;
        return newHead;
    }
}