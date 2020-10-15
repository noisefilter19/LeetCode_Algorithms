#include<stdio.h>
#include<math.h>

void main(){
  int n,orignal_number,remainder,result=0,count=0;
  printf("enter number\n");
  scanf("%d",&n);
  orignal_number=n;
  while(orignal_number!=0){
    orignal_number/=10;
    ++count;
  }
  orignal_number=n;
  while(orignal_number!=0){
    remainder=orignal_number%10;
    result+=pow(remainder,count);
    orignal_number/=10;
   }
  (result==n)?printf("armstrong number"):printf("not armstrong number");
}
