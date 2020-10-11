class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head==NULL || head->next==NULL){
            return head;
        }
        
        ListNode* dummy=new ListNode(0);
        dummy->next=head;
        ListNode* prev=dummy;
        
        while(head!=NULL && head->next!=NULL){
            ListNode* first=head;
            ListNode* second=head->next;
            //SWAPPING
            prev->next=second;
            first->next=second->next;
            second->next=first;
            //MOVE PREV AND HEAD
            prev=first;
            head=first->next;
        }
    return dummy->next;
    }
};
