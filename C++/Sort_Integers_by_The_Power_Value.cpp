class Solution {
public:
    class comp{
    public:
        bool operator()(pair<int,int> &p1, pair<int,int> &p2){
        
            if(p1.second == p2.second){
                return p1.first < p2.first;
            } 

            return p1.second < p2.second;

        }
    };
    
    
    int getKth(int lo, int hi, int k) {
        
        vector<pair<int,int>> res;
        
        for(int i = lo; i <= hi; i++){
            
            int num = i, step = 0;
            
            while(num != 1){
                
                if(num % 2 == 0){
                    num /= 2;
                } else {
                    num = 3*num + 1;
                }
                
                step++;
                
            }
            
            res.push_back(make_pair(i, step));
            
        }
        
        sort(res.begin(), res.end(), comp());
        
        return res[k-1].first;
        
    }
};
