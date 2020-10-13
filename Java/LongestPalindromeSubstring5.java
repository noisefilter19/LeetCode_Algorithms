// The problem was taken from : https://leetcode.com/problems/longest-palindromic-substring/
//
// Created by Ricky Benkovich 13/10/2020
//
public class LongestPalindromeSubstring5 {

    public String expandPalindrome(String s, int left, int right, String curr_pali, int i){
        while (s.charAt(left) == s.charAt(right)){

            if (curr_pali.length() == 0)
                if (left == right)
                    curr_pali = s.charAt(i) + "";
                else
                    curr_pali = s.charAt(left) + "" + s.charAt(right);
            else
                curr_pali = s.charAt(left) + curr_pali + s.charAt(right);
            left --;
            right ++;

            if (left < 0 || right >= s.length())
                break;
        }
        return curr_pali;
    }


    public String longestPalindrome(String s) {
        String max_Pali = "";

        for(int i = 0; i < s.length(); i++) {
            String pali_odd= "";
            String pali_even = "";

            pali_odd = expandPalindrome(s, i, i, pali_odd, i);
            if (i+1 < s.length())
                pali_even = expandPalindrome(s, i, i+1, pali_even, i);

            if (pali_odd.length() > max_Pali.length())
                max_Pali = pali_odd;

            if (pali_even.length() > max_Pali.length())
                max_Pali = pali_even;
        }
        return max_Pali;
    }
}


