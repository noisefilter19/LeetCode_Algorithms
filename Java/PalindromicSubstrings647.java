// This problem was taken from: https://leetcode.com/problems/palindromic-substrings/

public class PalindromicSubstrings647 {

    public int cnt_palindrome(String s, int left, int right, int i){
        int cnt = 0;
        while (s.charAt(left) == s.charAt(right)){
            cnt ++;
            left --;
            right ++;

            if (left < 0 || right >= s.length())
                break;
        }
        return cnt;
    }

    public int countSubstrings(String s) {
        int cnt = 0;
        for(int i = 0; i < s.length(); i++) {
            cnt += cnt_palindrome(s, i, i, i);
            if (i+1 < s.length())
                cnt += cnt_palindrome(s, i, i+1, i);
        }
        return cnt;

    }
}
