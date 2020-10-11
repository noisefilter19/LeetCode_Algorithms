/* Problem link ->  https://leetcode.com/problems/longest-valid-parentheses/  */


class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st;
        st.push(-1);
        int ans = 0;
        for(int i =0;i<s.size();i++)
        {
            char symb = s[i];
            if(symb=='(')
            {
                st.push(i);
            }
            
            else
            {
                st.pop();
                if(st.empty()) st.push(i);
                else ans = max(ans,i-st.top());
            }
        }
        
        return ans;
    }
};



// By - aditya113141
