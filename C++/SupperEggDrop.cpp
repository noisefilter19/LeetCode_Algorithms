#include<bits/stdc++.h>
/* Problem task : You are given K eggs, and you have access to a building with N floors from 1 to N. Each egg is identical in function, and if an egg breaks, you cannot drop it again.
You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.
Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 
Your goal is to know with certainty what the value of F is.
What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

Problem link : https://leetcode.com/problems/super-egg-drop/

*/


using namespace std;

int superEggDrop(int K, int N) {
        /*Create a 2D dp matrix where jth cell of ith row represents the minimum number of trials needed            to check i floors using j eggs. */
        
        int eggs = K, floors = N;
        
        vector<vector<int>> dp(floors+1,vector<int>(eggs+1,0));
        
        // case 1: when there are 0 floors
        for(int egg = 0; egg<=eggs; egg++) dp[0][egg] = 0;
        // case 2: when there are 1 floors
        for(int egg = 0; egg<=eggs; egg++) dp[1][egg] = 1;
        // case 3: when there are 0 eggs
        for(int floor=0; floor<=floors; floor++) dp[floor][0] = 0;
        // case 4: when there are 1 eggs
        for(int floor=0; floor<=floors; floor++) dp[floor][1] = floor;
        
        for(int egg=2; egg<=eggs; egg++) {
            for(int floor=2; floor<=floors; floor++) {
                int mn = INT_MAX;
                // choosing an ith floor between 1 to floor
                for(int i=1; i<=floor; i++) {
                // dp[i - 1][egg-1] means to find the answer when 
				// the egg is broken at ith floor
				// dp[floor - i][egg] means to find the answer 
				// when the egg is not broken at ith floor
                    int ans = 1 +  max(dp[i-1][egg-1],dp[floor-i][egg]);
                    mn = min(ans,mn);
                }
                dp[floor][egg] = mn;
            }
        }
        
        return dp[floors][eggs];
    }
  
int main(){
	int n,k;
	cin>>n>>k;
	cout<<supperEggDrop(k,n)<<endl;
	return 0;
}    
