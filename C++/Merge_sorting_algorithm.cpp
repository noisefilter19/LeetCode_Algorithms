#include <stdio.h>  
#include <stdlib.h>   
using namespace std;
 
void merge(int arr[], int l, int m, int r)  
{   
    int i, j, k;  
    int n1 = m - l + 1;  
    int n2 = r - m;  
  
    int L[n1], R[n2];  
  
    for (i = 0; i < n1; i++)  
        L[i] = arr[l + i];  
    for (j = 0; j < n2; j++)  
        R[j] = arr[m + 1 + j];  
    
	i = 0; // Initial index of first subarray  
    j = 0; // Initial index of second subarray  
    k = l; // Initial index of merged subarray  
    while (i < n1 && j < n2) 
	{  
        if (L[i] <= R[j]) {  
            arr[k] = L[i];  
            i++;  
        }  
        else {  
            arr[k] = R[j];  
            j++;  
        }  
        k++;  
    }  
    while (i < n1) 
	{  
        arr[k] = L[i];  
        i++;  
        k++;  
    }  
    while (j < n2) 
	{  
        arr[k] = R[j];  
        j++;  
        k++;  
    }  
}  
void mergeSort(int arr[], int l, int r)  
{  
    if (l < r) 
	{  
        int m = l + (r - l) / 2;  
        // Sort first and second halves  
        mergeSort(arr, l, m); 
		mergeSort(arr, m + 1, r);  
        merge(arr, l, m, r);  
		
    }  
}  
void printArray(int A[], int size)  
{  
    int i;  
    for (i = 0; i < size; i++)  
    printf("%d ", A[i]);  
    printf("\n");  
}  
int main()  
{  
    int n;
    printf("Enter the number of elements:");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the elements of arry:");
    int i,j;
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    int arr_size=n;
    mergeSort(arr, 0, arr_size - 1);  
    printf("\nSorted array is \n");  
    printArray(arr, arr_size);  
    return 0;  
}  