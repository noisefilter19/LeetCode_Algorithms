/**
 * Solution to Find the Duplicate Number at LeetCode in Javascript
 *
 * author: liady
 * ref: https://leetcode.com/problems/find-the-duplicate-number/
 */
function findDuplicate(nums) {
  const arr = [...nums];
  const len = arr.length;
  arr.forEach(num => {
    arr[num % len] = arr[num % len] + len;
  })
  let [max, maxInd] = [0, 0];
  arr.forEach((num, ind) => {
    if (num > max) {
      [max, maxInd] = [num, ind]
    }
  });
  return maxInd;
}
