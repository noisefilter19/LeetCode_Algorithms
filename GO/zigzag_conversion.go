// Link: https://leetcode.com/problems/zigzag-conversion/
func convert(s string, numRows int) string {
    s_size := len(s)
	ans := ""
	if numRows == 1 {
		return s
	}
	cycleLen := (numRows - 1) * 2;
	for i := 0; i < numRows; i++ {
		for j := 0; j < s_size-i; j = j + cycleLen {
			ans += string(s[j+i])
			if i != 0 && i != numRows-1 && j < s_size+i-cycleLen {
				ans += string(s[j-i+cycleLen])
			}
		}
	}
	return ans
}

