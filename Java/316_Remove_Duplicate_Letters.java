/*

Problem No: 316  Remove Duplicate Letters
URI: https://leetcode.com/problems/remove-duplicate-letters/
Logic: Maintain an array of length 26 to keep note of the index at which the letter in the given string is last observed
Next, build a stack such that the character pushed first is added if and only if it the last occurance and also the ascii value is less than the valuw previous,
Also maintain a visited array to handle multiple additions of same char to the stack.
*/

class Solution {
    public String removeDuplicateLetters(String s) {
        int[] result =new int[26];
        for(int i=0;i<s.length();i++){
            result[s.charAt(i)-97]=i;
        }
        boolean[] visited = new boolean[26];
        Stack<Character> stack = new Stack <>();
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(visited[c-'a']){
                continue;
            }
            while(!stack.isEmpty () && stack.peek()>c && result[stack.peek () - 'a']>i){
                visited[stack.peek () - 'a'] = false;
				stack.pop ();
            }
            // System.out.println(stack+"\t"+c);
            stack.push(c);
            visited[c-'a']=true;
            
        }
        StringBuilder ans = new StringBuilder ();
		
		while (!stack.isEmpty ()) {
			ans.append (stack.pop());
		}
		
		return ans.reverse().toString ();
    }
}