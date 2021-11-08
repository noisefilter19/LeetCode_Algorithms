Algorithm : Implementation

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int n =  nums.size();
        vector<int> res;
        for(int i=0; i<n;i++){
            int &x = nums[abs(nums[i])-1];
            if(x < 0){
                res.push_back(abs(nums[i]));
            } 
            // mark as already visited
            x = -x;
            
        }
        return res;
    }
};


/*
* 1. bruteforce = O(n2), O(1)
* 2. sort and 2 pointer method O(n + nlogn), O(1)
* 3. hash_table method O(n), O(n)
* 4. Solution O(n), O(1)
* variation
==========
* if only one element is duplicate?
* use floyd-cycle detection algorithm
==========
* numbers may not range between array indexes?
* use embeded hash table a[a[i]%n] += n; -- to update
*/
