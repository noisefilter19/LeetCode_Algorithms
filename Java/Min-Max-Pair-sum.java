class Solution {
    public int minPairSum(int[] nums) {
       Arrays.sort(nums);
        int l = 0;
        int r = nums.length - 1;
        int result = Integer.MIN_VALUE;
        while(l < r){
            int temp = nums[l++] + nums[r--];
            if(temp > result){
                result = temp;
            }
        }
        return result;
    }
}