// https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        ios::sync_with_stdio;
        int i = 0, j = 0;
        int mx = 0;
        int cl = 0;
        vector<int> mp(128, 0);
        while (j < s.length()) {
            char ch = s[j];
            i = mp[ch] > i ? mp[ch] : i;
            cl = j - i + 1;
            mx = mx>cl?mx:cl;
            mp[s[j]] = j + 1;
            j++;
        }
        return mx;
    }
};