class Solution {
public:
    void reorderList(ListNode* head) {
        if(head==NULL)
            return;
        ListNode* slow=head,*fast=head->next;
        while(fast && fast->next)
        {
            slow=slow->next;
            fast=fast->next->next;
        }
        ListNode* rev=slow->next;
        slow->next=NULL;
        ListNode* curr=rev,*prev=NULL,*next;
        while(curr!=NULL)
        {
            next=curr->next;
            curr->next=prev;
            prev=curr;
            curr=next;
        }
        rev=head;
        fast=head->next;
        int flag=0;
        while(fast || prev)
        {
            if(flag==0)
            {
                rev->next=prev;
                prev=prev->next;
                rev=rev->next;
                flag=1;
            }
            else
            {
                rev->next=fast;
                fast=fast->next;
                rev=rev->next;
                flag=0;
            }
        }
    }
};
