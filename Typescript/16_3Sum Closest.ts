/*
 * https://leetcode.com/problems/3sum-closest/
 */

function threeSumClosest(a: number[], target: number): number {
    let count = 0;
    let sum =0;
    var result = [];
    let closest = 0;

    for (var i = 0; i < a.length-2; i++) {
      for (var j = i+1; j< a.length-1;j++) {
        for (var k = j+1; k < a.length;k++) {
            let sum = a[i]+a[j]+a[k] 
             result.push(sum);
        }
      }
    }    
    
    closest = result.reduce((a, b) => {
        return Math.abs(b - target) < Math.abs(a - target) ? b : a;
    });

    console.log(closest);
    return closest;
};