//LeetCode Problem link - https://leetcode.com/problems/decode-ways/
class Solution
{
public:
    int numDecodings(string s)
    {
        int size = s.size();
        if (size == 0)
            return 0;
        if (s[0] == '0')
            return 0;
        int output[size + 1];
        output[0] = 1;
        output[1] = 1;
        for (int i = 2; i <= size; i++)
        {
            if (s[i - 1] == '0')
            {
                if (s[i - 2] == '1' || s[i - 2] == '2')
                    output[i] = output[i - 2];
                else
                    return 0;
            }
            else
            {
                output[i] = output[i - 1];
                if ((((s[i - 2] - '0') * 10 + (s[i - 1] - '0')) <= 26) && s[i - 2] != '0')
                    output[i] = ((output[i]) + (output[i - 2]));
            }
        }
        int ans = output[size];
        return ans;
    }
};