
#include<iostream>
#include<climits>
#include<bits/stdc++.h>

using namespace std;

// problem: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

static auto fast_io = [](){ 
    std::ios::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();

class Solution {
public:
    int shortestSubarray(vector<int>& A, int K) {
        int s = 0;
        int e = A.size() - 1;
        int ans = INT_MAX;
 
        vector<int> prefix{0};
        int n = A.size();
        for (int i = 0 ; i < n; i++)
            prefix.push_back (prefix.back() + A[i]);
        
        /*
        Thought Process
        A. 2 pointer approach won't work bcoz it only works when: 
            1. if we found an ans b/w i,j , we are sure that there will be a smaller length ans b/w i and j.
            2. if we found an ans b/w i,j , we are sure that there will be a bigger length ans b/w --i and ++j.
             But here , due to -ve numbers these constraints don't match and thus can't use this approach.

        B. Something to do with Prefix Sum maybe:
            - Cannot directly use prefix sum as again -ve numbers is the issue.
            - Found pattern(using pen n paper), that can only consider increasing values of the prefix sum t find the ans -> MONOTONIC QUEUE (q bcoz insert/delete from front and end in O(1)).
    */        
        deque<pair<int,int>> dq;  // monotonix DQ i.e continously increasing
        dq.push_back({0,-1});    // {prefix_sum_till_index , index}
        for (int i = 0 ; i <= n ; i ++) {
            if (dq.back().first >= prefix[i]) {
                while ( !dq.empty() && dq.back().first >= prefix[i])
                    dq.pop_back();
            }
            else {
                while ( !dq.empty() && prefix[i] - dq.front().first >= K) {
                    ans = min(ans, i-dq.front().second );
                    dq.pop_front();
                }                
            }
            dq.push_back( {prefix[i], i} );
        }
        return ans == INT_MAX ? -1 : ans;
    }
};

int main( int argc,  char *argv[]){
    vector<int> v {1,2,3,-4,5};
    int K = 3;
    cout << "Answer : " << Solution().shortestSubarray(v,K) << endl;
}
