// Unique Paths problem in C++
// Suppose there is a route in the form of a grid and we have to travel from the bottom left to the top right of this grid by moving only right and up.
// the following programme takes in the number of rows and columns in the grid route we have to travel and gives the number of unnique paths trhough which we can reach our destination.
// constant time complexity

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
