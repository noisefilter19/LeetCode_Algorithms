class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        
        //i and j cz transpose -> row reverse
        
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);
        
        
        //transpose matrix
        for(int i=0; i<matrix.size();i++){
            for(int j=i; j<matrix[i].size(); j++){
                swap(matrix[i][j], matrix[j][i]);
                
            }
        }
        
        //row reversal to get rotated image
        for(int i=0; i<matrix.size(); i++){
            reverse(matrix[i].begin(), matrix[i].end());
        }     
        
        
    }
};
