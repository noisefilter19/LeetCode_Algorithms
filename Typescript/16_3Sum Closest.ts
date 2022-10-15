/*
 * https://leetcode.com/problems/3sum-closest/
 */

function threeSumClosest(nums: number[], target: number): number {
    var result = [];
    let closest = 0;

    for (var i = 0; i < nums.length-2; i++) {
      for (var j = i+1; j< nums.length-1;j++) {
        for (var k = j+1; k < nums.length;k++) {
            let sum = nums[i]+nums[j]+nums[k] 
             result.push(sum);
        }
      }
    }    
    
    closest = result.reduce((a, b) => {
        return Math.abs(b - target) < Math.abs(a - target) ? b : a;
    });

    return closest;
};