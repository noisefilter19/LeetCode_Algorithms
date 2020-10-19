/**
 * @author KMuthusamyms
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let lastpos=nums.length-1;
    for(let i=nums.length-1;i>-1;i--){
        if(i+nums[i]>=lastpos){
            lastpos=i;
        }
    }
    return lastpos==0;
};
