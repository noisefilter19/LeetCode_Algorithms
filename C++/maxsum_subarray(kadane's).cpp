#include<bits/stdc++.h>
using namespace std;
int main() {

    int n;
    cin>>n;
    int a[1000];

    int csum=0;
    int mxsum=0;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    //kadane's algorithm
    for(int i=0;i<n;i++){
        csum += a[i];
        if(csum<0){
            csum=0;
        }
        mxsum = max(csum,mxsum);


    }
    cout<<"maximumSum is "<<mxsum<<endl;

	
	return 0;
}