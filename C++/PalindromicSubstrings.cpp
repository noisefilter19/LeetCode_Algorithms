//
// Created by Ofek Mula on 13/10/2020.
//
//
// Created by Ofek Mula on 13/10/2020.
//
class Solution {
public:
    int countSubstrings(string s) {
        int counter=0;
        int left_index=0;
        int right_index=0;
        for (int i=0; i<s.length();i++){
            left_index=i;
            right_index=i;
            count_palindrome(s,left_index,right_index,counter);
            if (right_index<s.length()-1) {
                count_palindrome(s,left_index,right_index+1,counter);
            }
        }

        return counter;
    }

    void count_palindrome(string s,int left_index,int right_index,int& counter){
        if (left_index>=0 && right_index <s.length()){
            while (s[left_index]==s[right_index] ){
                counter++;
                left_index = left_index-1;
                right_index = right_index+1;
                if (left_index<0 || right_index >= s.length()){
                    break;
                }
            }
        }
    }
};


