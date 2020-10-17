//https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3491/

class Solution
{
public:
    string removeDuplicateLetters(string s)
    {
        vector<int> freq(26, 0);
        vector<bool> visited(26, false);
        vector<char> result;
        for (int i = 0; i < s.size(); i++)
        {
            freq[s[i] - 'a']++;
        }
        for (char ch : s)
        {
            if (!visited[ch - 'a'])
            {
                visited[ch - 'a'] = true;
                if (result.size() > 0 && (ch < result[result.size() - 1]))
                {
                    char lastchar = result[result.size() - 1];
                    while (result.size() > 0 && ch < lastchar && freq[lastchar - 'a'] > 0)
                    {
                        visited[lastchar - 'a'] = false;
                        result.pop_back();
                        if (result.size() > 0)
                            lastchar = result[result.size() - 1];
                    }
                }
                result.push_back(ch);
            }
            freq[ch - 'a']--;
        }
        return string(result.begin(), result.end());
    }
};