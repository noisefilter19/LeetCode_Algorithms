// https://leetcode.com/problems/rotate-list/

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL)
            return head;
        else if (head->next == NULL)
            return head;
        vector<ListNode*> address;
        ListNode* temp = head;
        
        while(temp != NULL)
        {
            address.push_back(temp);
            temp = temp->next;
        }
        
        int r = k % address.size(); 
        cout << r << endl;
        if (r > 0)
        {
            int len = address.size();
            address[len-r-1]->next = NULL;
            address[len-1]->next = head;
            head = address[len-r];
        }
        return head;
    }
};