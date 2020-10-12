//https://leetcode.com/problems/unique-paths/

class Solution {
public:
    long int uniquePaths(int m, int n) {
    long int a=m-1, b=n-1;
    long int paths;
    long int total=a+b;
    long int smaller=0;
    if (a<=b)
    {
        smaller=a;
    }
    else
    {
        smaller=b;
    }
    long int numerator=1, denominator=1;
    for(long int i=0; i<smaller ; i++)
    {
        numerator *= (total-i);
        denominator *= i+1;
    }
    long int answer= numerator/ denominator;
    return answer;
        
    }
};
