
/*
1156. Swap For Longest Repeated Character Substring
- Given a string text, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.
Example 1:
Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.
Example 2:
Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.
*/

class Solution {
    public int maxRepOpt1(String text) {
        int[] freq=new int[26];
        for(int i=0;i<text.length();i++)
            freq[text.charAt(i)-'a']++;
        int s=0,maxcount=0,res=0;
        char maxchar='#';
        int[] count=new int[26];
        for(int f=0;f<text.length();f++){
            if(++count[text.charAt(f)-'a']>maxcount){
                maxcount=count[text.charAt(f)-'a'];
                maxchar=text.charAt(f);
            }
            while(f-s+1-maxcount>1)
                --count[text.charAt(s++)-'a'];
            res=Math.max(res,Math.min(freq[maxchar-'a'],f-s+1));
        }
        return res;
    }
}
