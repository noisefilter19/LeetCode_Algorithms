#include <iostream>
#include <stack>
using namespace std;
int main()
{
  int a,b,l,c;
  stack <int> stos;
  cout << "Number to change: ";
  cin >> a;
	l=a;

  while(a!=0)
  {
      b=a%2;
      a=a/2;
      stos.push(b);
  }
	cout << "Number " << l << " is equal to:  ";
    while(!stos.empty())
  {
      cout << stos.top();
      stos.pop();
  }
    cout << " in binary system.";

return 0;
}
