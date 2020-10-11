/* Problem link ->  https://leetcode.com/problems/longest-valid-parentheses/  */


class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st;

        int ans = 0,cur=0;
        for(int i =0;i<s.size();i++)
        {
            char symb = s[i];
            if(symb=='(')
            {
                st.push('(');
            }

            if(symb==')' and st.empty())
            {
                ans = max(ans,cur);
                cur  = 0;
            }

            else
            {
                cur+=2;
                st.pop();
            }


        }
        ans = max(ans,cur);
        return ans;
    }
};



// By - aditya113141
