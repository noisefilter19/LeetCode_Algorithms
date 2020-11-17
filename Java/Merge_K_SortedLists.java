/**Problem Desciption
 *  You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    Merge all the linked-lists into one sorted linked-list and return it.

    Problem link - https://leetcode.com/problems/merge-k-sorted-lists/
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
class Merge_K_SortedLists {
    public ListNode mergeKLists(ListNode[] lists) {
        int k=lists.length;
        ListNode sorted=new ListNode(0);
        if(lists.length==0)
            return sorted.next;
        PriorityQueue<ListNode> pq=new PriorityQueue<>(k,(a,b)->Integer.compare(a.val,b.val));
        ListNode ptr=sorted;
        for(int i=0;i<k;i++)
            if(lists[i]!=null)
                pq.add(lists[i]);
        while(!pq.isEmpty())
        {
            ListNode temp=pq.poll();
            ptr.next=temp;
            ptr=ptr.next;
            if(temp.next!=null)
            {
                temp=temp.next;
                pq.add(temp);
            }
            
        }
        return sorted.next;
    }
    
} 
