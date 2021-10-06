//Question:
/*
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Eg1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
*/

//Solution:

class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int>st,v;
        int count=0;
        for(int i=0;i<s.size();i++){
            cout<<count<<" : "<<i<<endl;
            if((s[i]==')') && ((st.size()!=0) && (s[st[st.size()-1]]=='('))){
                st.pop_back();
                count++;
            }
            else{
                st.push_back(i);
            }
            v.push_back(count);
        }
        cout<<count<<endl;
        if(st.size()==0){
            return count*2;
        }
        else{
            
            int maxx=v[st[0]];
            cout<<st[0]<<endl;
            for(int i=1;i<st.size();i++){
                cout<<st[i]<<endl;
                if(v[st[i]]-v[st[i-1]]>maxx){
                    maxx=v[st[i]]-v[st[i-1]];
                }
                cout<<"maxx: "<<maxx<<" "<<count<<" i: "<<i<<endl;
            }
            return max((count-v[st[st.size()-1]])*2,maxx*2);
        }
    }
};