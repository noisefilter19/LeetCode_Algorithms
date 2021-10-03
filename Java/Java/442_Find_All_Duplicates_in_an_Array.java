class Solution {
    public List<Integer> findDuplicates(int[] nums) {
      List<Integer> output = new ArrayList<Integer>();
      Arrays.sort(nums);
      for(int i=0; i<nums.length-1; i++){
        if( nums[i] == nums[i+1] ){
          output.add(nums[i]);
        }
      }
      
      return output;
    }
}
