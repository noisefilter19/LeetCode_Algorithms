// problem link: https://leetcode.com/problems/divide-two-integers/

// Runtime: 109 ms, faster than 48.23% of JavaScript online submissions for Divide Two Integers.

const divide = (dividend, divisor) => {
  if (dividend === -2147483648 && divisor === -1) return 2147483647
  let ans = 0
  let sign = 1
  if (dividend < 0) {
    dividend = -dividend
    sign = -sign
  }
  if (divisor < 0) {
    divisor = -divisor
    sign = -sign
  }
  if (dividend === divisor) return sign
  for (let i = 0, val = divisor; dividend >= divisor; i = 0, val = divisor) {
    while (val > 0 && val <= dividend) {
      val = divisor << ++i
    }
    dividend -= divisor << (i - 1)
    ans += 1 << (i - 1)
  }
  return sign < 0 ? -ans : ans
}
