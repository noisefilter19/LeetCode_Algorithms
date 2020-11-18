#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
ll l_search(vector<ll> arr,ll l,ll r,ll ele)
{
   ll pos=-1;
   while(l<=r)
   {
      ll mid=(l+r)/2;
      if(arr[mid]==ele)
      {
         pos=mid;
         break;
      }
      else if(arr[mid]>ele)
      {
         r=mid-1;
      }
      else
      {
         l=mid+1;
      }
      
   }
   return pos;
}
int main()
{
   ll n,t,k,i;
   cin>>t;                             //t-no. of test cases.
   while(t--)
   {
      cin>>n>>k;                       //n -number of elements and k difference.
      vector <ll> arr;
      map<ll,ll> mp;                    //hashmap to store counts.
      ll cnt=0,a;
      for(i=0;i<n;i++)
      {
         cin>>a;
         mp[a]++;
         if(mp[a]<2)
         {
            arr.push_back(a);
         }  
      }
      sort(arr.begin(),arr.end());
      for(i=0;i<arr.size();i++)
      {
         if(l_search(arr,i+1,n-1,arr[i]+k)!=-1)
         {
            cnt++;
         }
      }
      cout<<cnt<<endl;
   }
   return 0;
}
/* INPUT FORMAT
t
n k
arr[0],arr[1],arr[2]......arr[n-1].
*/
