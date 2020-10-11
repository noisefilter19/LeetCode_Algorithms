// Author: Fahim Muntashir

#include <iostream>

using namespace std;


int main()
{

    //your code will be  here to apply linear search

}

int linearSearch(int arr[], int size, int key)
{
    for (int i = 0; i < size; i++)
    {
        if (arr[i] == key)
        {
            return i;
        }
    }
    return -1;
}