// Unique Paths problem in C++
// Suppose there is a route in the form of a grid and we have to travel from the bottom left to the top right of this grid by moving only right and up.
// the following programme takes in the number of rows and columns in the grid route we have to travel and gives the number of unnique paths trhough which we can reach our destination.
// constant time complexity

#include<iostream>
using namespace std;

void uniquepaths(int m, int n)
{
    int paths;
    int total=m+n;
    int smaller=0;
    if (m<=n)
    {
        smaller=m;
    }
    else
    {
        smaller=n;
    }
    int numerator=1, denominator=1;
    for(int i=0; i<n ; i++)
    {
        numerator *= (total-i);
        denominator *= i+1;
    }
    int answer= numerator/ denominator;
    cout<<"the number of paths to  traverse such a grid is: "<<answer;
}

int main()
{
    cout<<"enter the number of columns and rows in the grid you want to traverse"<<endl;
    int a, b;
    cin>>a;
    cout<<endl;
    cin>>b;
    cout<<endl;
    uniquepaths(a-1,b-1);
    int n;
    cin>>n;
    return 0;

}

