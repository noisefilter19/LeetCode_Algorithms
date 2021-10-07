// Problem Link : https://leetcode.com/problems/count-primes/

class Solution {
public:
    int countPrimes(int n) {
        long long int i, j, ans = 0;
        vector <bool> isprime(n + 1, true); // true if prime otherwise false
        isprime[0] = isprime[1] = false; // 0, 1 are not prime numbers

//         Using seive of erathosthenes to find the prime number numbers in the range from 1 to n
        for (i = 2; i * i <= n; i++)
        {
            if (isprime[i])
            {
                for (j = i * i; j <= n; j = j + i) // once i * i >= n, then j = j + i always > n, so use of checking those index / numbers
                {
                    isprime[j] = false;
                }
            }
        }

        for (i = 1; i < n; i++) // Checking which all are primes numbers till n (n excluded)
        {
            if (isprime[i])
                ans++;
        }

        return ans;
    }
};
