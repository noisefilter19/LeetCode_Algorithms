#include <iostream>
#include <vector>

using namespace std;
int countPrimes(int n) {
        vector<bool>isPrime(n + 1, true);
        isPrime[0] = isPrime[1] = false;
        
        for(int i = 2; i*i <= n; i++) {
            if(!isPrime[i]) continue;
            for(int j = i*i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
        
        int count = 0;
        
        for(int i = 2; i < n; i++) {
            if(isPrime[i]) count++;
        }
        return count;
    }
    
int main(){
    int n;
    cin>>n;
    countPrimes(n);
    cout<<countPrimes(n);
    return 0;
};