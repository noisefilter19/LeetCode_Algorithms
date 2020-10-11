//  https://leetcode.com/problems/powx-n/

double myPow2(double x,int n){
    double value;
    if(n==0)
        return 1;
    else{
        value=myPow2(x,n/2);
        if(n%2==0)
            return value*value;
        else
            return value*value*x;
    }
}

double myPow(double x, int n){
    double exp;
    exp=myPow2(x,n);
    if(n>=0)
        return exp;
    else
        return 1/exp;
}
