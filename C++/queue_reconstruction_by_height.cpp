bool comp(vector<int> a, vector<int> b) {
    return a[0]<b[0];
}
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        vector<vector<int>> ret(people.size());
        sort(people.begin(),people.end(),comp);
        for(vector<int> v: people) {
            cout<<v[0]<<" "<<v[1]<<endl;
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