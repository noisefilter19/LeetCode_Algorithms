Problem Statement:

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


CODE:


class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();

        int[] dp = new int[n + 1];

        for(int j = 0; j <= n; j++) {
            dp[j] = j;
        }

        for(int i = 1; i <= m; i++) {
            int[] newDp = new int[n + 1];
            newDp[0] = i;
            for(int j = 1; j <= n; j++) {
                if(word1.charAt(i - 1) == word2.charAt(j - 1))
                    newDp[j] = dp[j - 1];
                else
                    newDp[j] = min(dp[j - 1] + 1, dp[j] + 1, newDp[j - 1] + 1);
            }
            dp = newDp;
        }
        return dp[n];
    }

    private int min(int a, int b, int c) {
        if(a <= b && a <= c) return a;
        else if (b <= a && b <= c) return b;
        else return c;
    }
}
