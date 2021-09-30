//
// Created by Ofek Mula on 14/10/2020.
//

#include <stdio.h>
#include <string.h>

char* get_substring(char* s,int start_index,int end_index){
    char* substring=(char*)malloc(sizeof(char)*(end_index-start_index+2));
    for ( int i=start_index;i<=end_index;i++){
        substring[i-start_index]=s[i];
    }
    substring[end_index-start_index+1]='\0';
    return substring;
}

char* get_palindrome(char* s,int left_index,int right_index){
    char* palindrome;
    if (left_index>=0 && right_index <strlen(s)){
        while (s[left_index]==s[right_index] ){
            palindrome=get_substring(s,left_index,right_index);
            left_index = left_index-1;
            right_index = right_index+1;
            if (left_index<0 || right_index >= strlen(s)){
                break;
            }
        }
    }
    return palindrome;
}

char* longestPalindrome(char *s){

    char* max_palindrome="";
    char* even_palindrome="";
    char* odd_palindrome="";
    int left_index;
    int right_index;
    int counter=0;
    for (int j=1;j<strlen(s);j++){
        if (s[0]==s[j]){
            counter++;
        }
    }
    if(counter==strlen(s)-1){
        return s;
    }
    for (int i=0; i<strlen(s);i++){

        left_index=i;
        right_index=i;
        odd_palindrome=get_palindrome(s,left_index,right_index);
        if (right_index<strlen(s)-1) {
            if (s[i] == s[i+1]){
                even_palindrome=get_palindrome(s,left_index,right_index+1);
            }
        }
        if (strlen(odd_palindrome) > strlen(max_palindrome)) {
            max_palindrome=odd_palindrome;
        }
        if (strlen(even_palindrome) > strlen(max_palindrome) ){
            max_palindrome=even_palindrome;
        }
    }
    return max_palindrome;
}
