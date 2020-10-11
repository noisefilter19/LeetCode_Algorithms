// Link: https://leetcode.com/problems/generate-parentheses/
func generateParenthesis(n int) []string {
    combinations := []string{}
    backtrack(&combinations, n, "", 0, 0 )
    return combinations
}

func backtrack(combinations *[]string, n int, currString string, open int, close int)  {
	if len(currString) == 2*n {
		*combinations = append(*combinations, currString)
		return
	}

	if (open < n) {
		backtrack(combinations, n, currString + "(", open + 1, close)
	}
	if (close < open) {
		backtrack(combinations, n, currString + ")", open, close + 1)
	}
	return
}

