/*
 * https://leetcode.com/problems/house-robber-ii/
 */

/**
 * @param {numbers[]} nums
 * @return {number}
 */
const helper = (nums) => {
    // init max array with nums length
    let max_array = new Array(nums.length);
    // max_array = dp
    // we iterate through nums and
    // we save only the highest value of either the { current house + 2 houses before } or the { house before }
    for (i in nums) {
        if (i == 0) max_array[i] = nums[i];
        if (i == 1) max_array[i] = Math.max(nums[0], nums[1]);
        if (i >= 2) max_array[i] = Math.max(nums[i] + max_array[i - 2], max_array[i - 1]);
    }
    return max_array[max_array.length - 1];
};

const rob = (nums) => {
    if (nums.length === 0) return 0;
    if (nums.length === 1) return nums[0];
    let start1 = [...nums];
    let start2 = [...nums];

    // circular, so the last house touches the first, therefore we do two runs of House Robber 1 (now helper)
    start1.pop();
    start2.shift();

    let max_start1 = helper(start1);
    let max_start2 = helper(start2);

    return Math.max(max_start1, max_start2);
};

// let nums = [1, 2, 3, 1];
// let nums = [];
// let nums = [];
// let nums = [11, 2];
// let nums = [1, 2, 3];
// let nums = [1, 2, 3, 4];
// let nums = [15, 2, 3];
let nums = [2, 7, 9, 3, 1];
console.log(rob(nums));
