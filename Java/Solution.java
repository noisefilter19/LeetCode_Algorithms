package start;
import java.util.*;

class Solution {
    public List<List<Integer>> permute(int[] nums) {
                int len = nums.length;
        List<List<Integer>> res = new ArrayList<>();
        Helper(nums, len, res);
        return res;

    }
        public void Helper(int[] input, int length, List<List<Integer>> result) {
    if (length == 1) {
      List<Integer> tmp = new ArrayList<>();
      for (Integer in : input) {
        tmp.add(in);
      }
      result.add(tmp);
      return;
    }
    for (int i = 0; i < length; i++) {
      Helper(input, length - 1, result);
      if (length % 2 == 1) {
        int tmp = input[0];
        input[0] = input[length - 1];
        input[length - 1] = tmp;
      } else {
        int tmp = input[i];
        input[i] = input[length - 1];
        input[length - 1] = tmp;
      }
    }
  }

}