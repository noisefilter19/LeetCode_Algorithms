public int minPairSum(int[] nums) {
        
        Arrays.sort(nums);
        int result = Integer.MIN_VALUE;
        
        for(int i = 0 ; i < nums.length/2;i++){
            result = Math.max(nums[i]+nums[nums.length-1 -i],result);
        }
        return result;
    }
