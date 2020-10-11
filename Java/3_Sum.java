//Problem Link: https://leetcode.com/problems/3sum/

//Solution

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int i, j;
        Arrays.sort(nums);
    
        List<List<Integer>> res = new ArrayList() ;
        
        for(int k = 0 ; k < nums.length-1 ; k++){
            i =k+1;
            j = nums.length-1;
            int ele = nums[k];
            
            if(  k > 0 && nums[k] == nums[k-1])  continue;
            
            while( i < j){
                
                if(  i-1 > k &&  nums[i] == nums[i-1] ){
                    i++;
                    continue;
                }
                
                if( -ele == nums[i] + nums[j] ){
                    List<Integer> list = new ArrayList();
                    list.add(ele);
                    list.add(nums[i]);
                    list.add(nums[j]);
                    
                    res.add( new ArrayList(list) );
                    i++;
                    j--;
                }
                else if( -ele > nums[i] + nums[j] )
                    i++;
                else 
                    j--;                                   
            }
        } 
        return res;
    }
}