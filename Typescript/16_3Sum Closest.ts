/*
 * https://leetcode.com/problems/3sum-closest/
 */

function threeSumClosest(nums: number[], target: number): number {
    let count = 0;
    let sum =0;
    let result = 0;
    for (count; count<3; count++){
        result = nums.reduce((a, b) => {
            return Math.abs(b - target) < Math.abs(a - target) ? b : a;
        });
        nums.splice(nums.indexOf(result), 1); 
        sum=sum+result;
    }
    return sum;
};