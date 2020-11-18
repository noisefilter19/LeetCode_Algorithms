/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
      ListNode *curr = nullptr;
      ListNode *ret = curr;
      
      while (!lists.empty()) {
        ListNode *tmp = new ListNode(INT_MAX);
        int loc = -1;
        for (int i = 0; i < lists.size(); ++i) {
          //cout << i ;
          if (lists[i] != nullptr) {
            //cout << lists[i]->val << endl;
            if (lists[i]->val < tmp->val) { 
              tmp = lists[i]; 
              loc = i;
            }
          } else {
            lists.erase(lists.begin() + i);
            --i;
          }
        }
        cout << endl;
        if (loc == -1) { return ret; }
        if (curr == nullptr) { 
          curr = tmp; 
          ret = curr;
        }
        else { 
          curr->next = tmp;
          curr= curr->next;
        }
        //cout << lists[loc]->val << endl;
        lists[loc] = lists[loc]->next;
        if (lists[loc] == nullptr) {
          lists.erase(lists.begin() + loc);
        }
      }
      return ret;
    }
};