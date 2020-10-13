//https://leetcode.com/problems/remove-nth-node-from-end-of-list/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int size = 1;
        ListNode *temp = head;
        while(temp->next != NULL){
            size++;
            temp= temp->next;
        }
        
        ListNode* temp2 = head;
        
        //edge case
        if(size == n){
            ListNode* temp4 = head;
            head = head->next;
            delete temp4;
            return head;
        }
        
        int counter = (size - n);
        
        for(int i=1; i<counter; i++){
            temp2 = temp2->next;    
        }
        
        if(temp2->next == NULL){
            
        }
        
        ListNode* temp3 = temp2->next;
        temp2->next = temp2->next->next;
        delete temp3;
        
        return  head;
    }
};