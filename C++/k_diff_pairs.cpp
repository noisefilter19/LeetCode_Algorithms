#include<bits/stdc++.h>
using namespace std;
 
int countPairs(int arr[], int n, int k)
{
    int pairs_count = 0;
    for (int i = 0; i < n; i++)
    {       
        for (int j = i+1; j < n; j++)
            if (arr[i] - arr[j] == k || arr[j] - arr[i] == k )
                  pairs_count++;
    }
    return pairs_count;
}

int main()
{
    int test_arr[] =  {1, 5, 3, 4, 2};
    int n = 5;
    int k = 4;
    cout << "Count of pairs with given diff is " << countPairs(test_arr, n, k);
    return 0;
}