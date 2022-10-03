// link:  https://leetcode.com/problems/sum-of-even-numbers-after-queries/
class SumOfEvenNumbersAfterQueries {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int initialSum = 0;
        for (int i : nums) {
            if (i % 2 == 0) {
                initialSum += i;
            }
        }
        // System.out.println("init: " + initialSum);
        int[] ans = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int oldValue = nums[queries[i][1]];
            nums[queries[i][1]] += queries[i][0];
            initialSum = evenSum(nums, queries[i][1], queries[i][0], nums[queries[i][1]], initialSum, oldValue);
            // System.out.println(MessageFormat.format("oldValue = {0}, newValue = {1}, nums
            // = {3}",oldValue,nums[queries[i][1]]));
            // System.out.println(Arrays.toString(ans));
            ans[i] = initialSum;
        }
        return ans;
    }

    private int evenSum(int[] arr, int modifiedIndex, int newValue, int modifiedValue, int initialSum, int oldValue) {
        if (modifiedValue % 2 == 0) {
            if (oldValue % 2 == 0) {
                initialSum = initialSum - oldValue + modifiedValue;
            } else {
                initialSum = initialSum + modifiedValue;
            }
        } else {
            if (oldValue % 2 == 0) {
                initialSum -= oldValue;
            }
        }
        return initialSum;
    }
}