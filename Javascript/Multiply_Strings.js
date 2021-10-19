// problem link: https://leetcode.com/problems/divide-two-integers/

// Runtime: 92 ms, faster than 66.27% of JavaScript online submissions for Multiply Strings.

const multiply = (num1, num2) => {
  let n1 = num1
  let n2 = num2

  if (parseInt(n1) === 0 || parseInt(n2) === 0) {
    return '0'
  }

  n1 = n1.split('').reverse()
  n2 = n2.split('').reverse()
  const result = []

  for (let i = 0; n1[i] >= 0; i++) {
    for (let j = 0; n2[j] >= 0; j++) {
      if (!result[i + j]) {
        result[i + j] = 0
      }

      result[i + j] += n1[i] * n2[j]
    }
  }

  for (let i = 0; result[i] >= 0; i++) {
    if (result[i] >= 10) {
      if (!result[i + 1]) {
        result[i + 1] = 0
      }

      result[i + 1] += parseInt(result[i] / 10)
      result[i] %= 10
    }
  }

  return result.reverse().join('')
}
