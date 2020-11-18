//Choose coins to obtain maximum output from the given piles(operate as stack)

class Solution {
public:
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(),piles.end(),greater<int>());
        int n = piles.size()/3;
        int sum = 0;
        for(int i=1;i<piles.size();i+=2){
            if(n){
                sum+=piles[i];
                n--;
            }
        }
        return sum;
    }
};