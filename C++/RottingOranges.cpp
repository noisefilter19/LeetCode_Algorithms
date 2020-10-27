class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {

        bool flag=false;
        int minutes_counter=0;
        if(is_all_rotten(grid)){
            minutes_counter= 0;
            return minutes_counter;
        }
        while(!flag && minutes_counter<=grid.size()*grid[0].size()){
            update(grid,flag);
            minutes_counter++;
        }
        if(flag==false){
            return -1;
        }
        return minutes_counter;


    }
    void update(vector<vector<int>>& grid,bool& flag){
        vector<vector<int>> updated_grid(grid);
        for ( int i=0;i<grid.size();i++){
            for(int j=0;j<grid[i].size();j++){
                if(grid[i][j]==2){//rotten  

                    if(i<grid.size()-1 ){
                        near_rotten_function(updated_grid[i+1][j]);
                    }
                    if(i>0){
                        near_rotten_function(updated_grid[i-1][j]);
                    }
                    if(j<grid[i].size()-1){
                        near_rotten_function(updated_grid[i][j+1]);
                    }
                    if(j>0){
                        near_rotten_function(updated_grid[i][j-1]);
                    }

                }
            }
        }
        grid=updated_grid;
        if(is_all_rotten(grid)){
            flag=true;
        }
    }
    void near_rotten_function(int& cell){
        if (cell==0){
            cell= 0;
            return;
        }
        cell=2;
    }
    bool is_all_rotten(vector<vector<int>>& grid){
        for (int i=0;i<grid.size();i++){
            for(int j=0;j<grid[i].size();j++){
                if (grid[i][j]==1){
                    return false;
                }
            }
        }
        return true;
    }
};
