// Leetcode 78 - Subsets in Java
/**
* Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
*/

import java.util.*;
public class Subsets {
	class Solution {
		public List<List<Integer>> subsets(int[] nums) {
			List<List<Integer>> subsets = new ArrayList<>();

			if (nums == null || nums.length == 0) {
				return subsets;
			}

			getSubsets(0, nums, new ArrayList<Integer>(), subsets);
			return subsets;
		}

		private void getSubsets(int index, int[] nums, List<Integer> current, List<List<Integer>> subsets) {
			subsets.add(new ArrayList<>(current));

			for (int i = index; i < nums.length; i++) {
				current.add(nums[i]);
				getSubsets(i + 1, nums, current, subsets);
				current.remove(current.size() - 1);
			}
			return;
		}
	}
}
