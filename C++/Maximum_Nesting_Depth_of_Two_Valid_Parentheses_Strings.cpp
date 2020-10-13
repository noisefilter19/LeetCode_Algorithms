/*Leetcode link: https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/ */

//The Question itself is simple but the wording makes it difficult
//What the question asks is, we have to make two VPS strings out of a parent string which is also VPS such that there depth of parantheses is minimum

class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
    
        int n=0,m=0;    //assuming n,m denoting the size A,B [for understanding take it as size of stack<string> A,B]
        vector<int> res;    //vector representing result
        for(int i=0;i<seq.size();i++)
            if(seq[i]=='('){
                if(n==m){  //whenever the size of A==B we increment count of B
                    n++;  
                    res.push_back(0); //here in ques, B is said to represent 0 in ans 
                 }
                else{
                    m++;  //whenever the size of A<B we increment count of A
                    res.push_back(1);  //here in ques, A is said to represent 1 in ans
                 }
              }
            else{
                if(n>m){
                    n--;   //whenever the size of B>A we decrement count of A
                    res.push_back(0);  //here in ques, B is said to represent 0 in ans 
                  }           
                else {
                    m--;   //whenever the size of A>=B we decrement count of A
                    res.push_back(1);  //here in ques, A is said to represent 1 in ans
                  }
        }
        return res;
                
    }
};
