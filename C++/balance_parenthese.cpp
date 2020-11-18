#include <iostream>
#include <stack>
#include <string>
#include <string.h>
using namespace std;
int main()
{
    stack<char> stack;
    string parenthese;
    cin >> parenthese;
    for (int i = 0; i < parenthese.size(); i++)
    {
        if (parenthese[i] == '(' || parenthese[i] == '[' || parenthese[i] == '{') {
            stack.push(parenthese[i]);
        }
        else if ((parenthese[i] == ')' && stack.top() == '(') 
            || (parenthese[i] == ']' && stack.top() == '[') 
            || (parenthese[i] == '}' && stack.top() == '{')) {
                stack.pop();
                if (stack.empty()) {
                    cout << "Balance" << endl;
                    break;
                }
            }
        
        else {
            cout << "Not balance" << endl;
            break;
        }
    }
}
