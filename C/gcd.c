#include <stdio.h>

int gcd(int, int);

int main()
{
    int a, b, result;

    printf("Enter the two numbers to find their GCD: ");
    scanf("%d%d", &a, &b);

    result = gcd(a, b);
    printf("The GCD of %d and %d is %d.\n", a, b, result);
}

int gcd(int a, int b)
{
    if(b==0)
     return a;
     else return gcd(b,a%b);
}
