//https://leetcode.com/problems/queue-reconstruction-by-height/

bool comp(vector<int> a, vector<int> b) {
    return a[0]<b[0];
}
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        vector<vector<int>> ret(people.size());
        sort(people.begin(),people.end(),comp);
        for(vector<int> v: people) {
            int x = v[1];
            for(int i=0;i<ret.size();i++) {
                if(ret[i].size()==0 || ret[i][0]==v[0]) {
                    x--;
                }
                if(x<0){
                    ret[i]=v;
                    break;
                }
            }
        }
        return ret;
    }
};

/*
 * consider the pair p<i,j> where i=height and j=no. of people with height >= height of p
 * first we place all the shortest height pairs to position j because they will anyway have someone with height >= their height
 * Then we place second shortest height and so on
 * suppose the pair p<i,j> is being processed
 * we need to keep p at jth empty position so x=j
 * we decrement x whenever we find an empty position or someone with same height because at empty postion there will be someone 
 * with height >= height of p
 * Need not to check for >= condition as we have sorted the array before so no one in ret array would be having height > height * of p 
 */
