//
// Created by Ofek Mula on 14/10/2020.
// s_i = start_index
// e_i = end_index
// l_i = left index
// r_i = right index
// p = palindrome
// m_p = max_palindrme
// o_p = odd_palindrome
// e_p = even_palindrome
// g_p = get_palindrome

#include <stdio.h>
#include <string.h>

char* get_substring(char* s,int s_i,int e_i){
    char* substring=(char*)malloc(sizeof(char)*(e_i-s_i+2));
    for ( int i=s_i;i<=e_i;i++){
        substring[i-s_i]=s[i];
    }
    substring[e_i-s_i+1]='\0';
    return substring;
}

char* g_p(char* s,int l_i,int r_i){
    char* p;
    if (l_i>=0 && r_i <strlen(s)){
        while (s[l_i]==s[r_i] ){
            p=get_substring(s,l_i,r_i);
            l_i = l_i-1;
            r_i = r_i+1;
            if (l_i<0 || r_i >= strlen(s)){
                break;
            }
        }
    }
    return p;
}

char* longestP(char *s){

    char* m_p="";
    char* e_p="";
    char* o_p="";
    int l_i;
    int r_i;
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

        l_i=i;
        r_i=i;
        o_p=g_p(s,l_i,r_i);
        if (r_i<strlen(s)-1) {
            if (s[i] == s[i+1]){
                e_p=g_p(s,l_i,r_i+1);
            }
        }
        if (strlen(o_p) > strlen(m_p)) {
            m_p=o_p;
        }
        if (strlen(e_p) > strlen(m_p) ){
            m_p=e_p;
        }
    }
    return m_p;
}
