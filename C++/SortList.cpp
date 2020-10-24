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
    ListNode* sortList(ListNode* head) {
        vector<int> v;
        ListNode *tmp = head;
        while(tmp!=NULL){
            v.push_back(tmp->val);
            tmp = tmp->next;
        }
        sort(v.begin(),v.end());
        int i=0;
        tmp=head;
        while(i<v.size()){
            tmp->val = v[i++];
            tmp=tmp->next;
        }
        return head;
    }
};