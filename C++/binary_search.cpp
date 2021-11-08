// Author: Fahim Muntashir


#include <iostream>
#include <bits/stdc++.h>

using namespace std;
int binarySearch(int *arr, int size, int search);

int main()
{

    //your code will be  here to apply linear search
}

int binarySearch(int *arr, int size, int search)
{
    int low = 0, high = size - 1, mid;

    while (low <= high)
    {
        mid = (low + high) / 2;

        if (search == arr[mid])
        {
            return mid;
        }
        else if (search > arr[mid])
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }

    return -1;
}