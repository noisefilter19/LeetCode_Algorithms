/*
 * https://leetcode.com/problems/palindrome-number/
 */

/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
    let arrayNum = Array.from(String(x), x => Number(x))
    
    return parseInt(arrayNum) === parseInt(arrayNum.reverse())
};
