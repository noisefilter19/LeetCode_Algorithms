//Leetcode Problem Link:https://leetcode.com/problems/counting-bits/



class Solution {
public:
    double myPow1(double x,int n){
       
        if(n==0){
            return 1;
        }
        else{
       
          double y=myPow1(x,n/2);
          //For Even Numbers
            if(n%2==0){
                return y*y;
            }
           //For Odd Numbers
            else{
                return x*y*y;
            }
        }
        
        
    }
    
    double myPow(double x, int n) {
    //Calling myPow1 
      double ans=  myPow1(x,n);
        if(n>=0){
            return ans;
        }
        else{
            return (1/ans);
        }
        
        
    }
};
