class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        priority_queue<pair<int, int> > p;
        int cur=nums[0];
        int freq=1;
        for(int i=1;i<nums.size();i++){
           if(nums[i]==cur){
               freq++;
           }else{
               p.push(make_pair(freq, cur));
               cur=nums[i];
               freq=1;
           }
        }
        p.push(make_pair(freq, cur));
        vector<int> res;
        for(int i=0;i<k;i++){
            res.push_back(p.top().second);
            p.pop();
        }
        return res;
    }
};
