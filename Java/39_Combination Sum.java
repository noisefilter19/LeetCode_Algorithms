/*

Problem No: 39  Combination Sum
URI: https://leetcode.com/problems/combination-sum/
Logic:  Sort the array and the explore all the possibilites of the subarrays and positions including the repetions of the arrays that can happen and 
then compute its sum if the sum is greater than the target, as the array was sorted we backtrack to the previous possiblity and if the sume is equal 
to the target the we add the subarray to the result. And we finally return the result.
*/

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        recurr(result,new ArrayList<>(),target,candidates,0);
        return result;
    }
    public void recurr(List<List<Integer>> result,List<Integer> currResult,int target,int[] candidates,int pos){
        int currSum = sumList(currResult);
        if(currSum>target){
            return;
        }
        else if(currSum==target){
            result.add(new ArrayList<>(currResult));
            return;
        }      
        for(int i=pos;i<candidates.length;i++){
            currResult.add(candidates[i]);
            recurr(result,currResult,target,candidates,i);
            currResult.remove(currResult.size()-1);
        }
        return;
    }
    public int sumList(List<Integer> nums){
        int res = 0;
        for(int i=0;i<nums.size();i++){
            res+=nums.get(i);
        }
        return res;
    }
}