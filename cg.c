#include <stdio.h>
int main()
{
  int n,r,sum=0;
  printf("enter no");
  scanf("%d",&n);
  while(n>0)
  {
     r=n%10;
     sum=sum+(r*r*r);
     n=n/10;
  }
  if(sum==n)
  {
      printf("armstrong");
  }
  else
  {
      printf("not");
  }
    return 0;
}

