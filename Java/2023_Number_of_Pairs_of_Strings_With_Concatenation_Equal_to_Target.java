class Solution {
    public int numOfPairs(String[] nums, String target) {
        HashSet<String> set = new HashSet<>();
        int n = nums.length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            for(int j=0; j<n; j++) {
                if(i!=j && target.equals(nums[i]+nums[j]) )
                    set.add(i + " " + j);
            }
        }
        return set.size();
    }
}
