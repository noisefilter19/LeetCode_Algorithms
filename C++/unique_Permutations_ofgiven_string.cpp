#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define ll long long int
#define ld long double
#define pb push_back
#define ff first
#define ss second
#define all(x) x.begin(), x.end()
#define mp map<ll, ll>
#define um unordered_map<ll, ll>
#define pll pair<ll, ll>
#define st set<ll> 
#define us unordered_set<ll>
#define vt vector<ll>
#define vp vector<pll>
#define fl(i, x, y) for(long i=x;i<y;++i)
#define flr(i, x, y) for(long i=x;i>=y;--i)

void permute(char *input,ll i,set<string> &s)
{
    if(input[i]=='\0')
    {
        cout<<input<<endl;
        string str(input);
        s.insert(str);
        return;
    }

    ll j;
    for(j=i;input[j]!='\0';j++)
    {
        swap(input[i],input[j]);
        permute(input,i+1,s);
        swap(input[i],input[j]);
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    ll i,j,k,l,e,n,m,t;
    
    cin>>t;

    while(t--)
    {
       
       char input[1000];
       cin>>input;
    
      set<string> s;
       permute(input,0,s);
    cout<<"unique permutations \n";
    for(auto itr:s)
    cout<<itr<<" ";
    cout<<endl;
    }
return 0; 
}
