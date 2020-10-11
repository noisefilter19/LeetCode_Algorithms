

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        n *= 2;
        vector<string> ans;
        cout << ( 1 << n) << endl;
        for(int i = 0; i < (1 << n); i ++) {
            string s = "";
            for(int j = 0; j < n; j ++) {
                if((i & (1 << j)))
                    s += '(';
                else
                    s += ')';
            }
            bool valid = true;
            int open = 0;
            for(auto x : s) {
                if(x == '(')
                    open++;
                else if (open)
                    open--;
                else
                    valid = false;
            }
            if(valid && ! open)
                ans.push_back(s);
        }
        return ans;
    }
};
