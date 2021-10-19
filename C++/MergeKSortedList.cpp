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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode *root=NULL;
        for(int i=0;i<lists.size();i++)
        {
            root=mergeTwoLists(root,lists[i]);
        }
        return root;
    }
    
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1==NULL){
            return l2;
        }
        if(l2==NULL){
            return l1;
        }
        ListNode *res=NULL,*root;
        if(l1->val<l2->val){
            res=l1;
            l1=l1->next;
        }else{
            res=l2;
            l2=l2->next;
        }
        root=res;
        while(l1&&l2){
            if(l1->val<l2->val){
                res->next=l1;
                res=res->next;
                l1=l1->next;
            }else{
                res->next=l2;
                res=res->next;
                l2=l2->next;
            }
        }
        if(l1){
            res->next=l1;
        }
        if(l2){
            res->next=l2;
        }
        return root;
    }
};
