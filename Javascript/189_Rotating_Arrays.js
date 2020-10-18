/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */

var rotate = function (nums, k) {
    let lastElement;
    while (k != 0) {
        lastElement = nums.pop();
        nums.unshift(lastElement);
        console.log(nums);
        return rotate(nums, k - 1);
    }
};

//  Example 1:
console.log("Example 1: ");
let nums = [1, 2, 3, 4, 5, 6, 7], k = 3;

rotate(nums, k);

// Example 2:
console.log("Example 2: ");
let numsTwo = [-1, -100, 3, 99], k_two = 2;

rotate(numsTwo, k_two);


