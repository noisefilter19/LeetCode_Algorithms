//https://leetcode.com/problems/rotate-array/
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        
           ios_base::sync_with_stdio(false);
                                    cin.tie(0);
                                    cout.tie(0);
        //O(n) solution
        
                            vector<int> ans(nums);
                            int n = nums.size();
                        
                            for(int i=0 ;i<n; i++){
                                nums[ (i+k)%n ] = ans[i]; 
                            }
        

                    //     nums = ans;
        
        //Second, INPLACE O(1) space solution
        
//                                     ios_base::sync_with_stdio(false);
//                                     cin.tie(0);
//                                     cout.tie(0);

//                                    int n = nums.size();     //initially 7
//                                    int x = k;
//                                    int i=0;
                                    
//                                    if(k==0)
//                                        return;
//                                    for(int j=n-k; j<n; j++){
//                                        if(k > 0){
//                                           swap(nums[i], nums[j]);
//                                            i++;
//                                            k--;              
//                                           }
//                                         }

//                                     vector<int>::iterator it1, it2; 

//                                     it1 = nums.begin()+i;
//                                       while(i< n-x){
//                                        int temp =  nums[i];
//                                        nums.push_back(temp);

//                                        i++;
//                                         }
//                                     it2 = nums.begin()+i;

//                                     nums.erase(it1,it2);

                               
     
        
//     while(k--){
//         nums.insert(nums.begin(), nums[nums.size()-1]);
//         nums.pop_back();
//     }
  
        
    }
};
