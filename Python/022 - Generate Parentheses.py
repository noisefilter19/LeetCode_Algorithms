"""
Topics: | String | Backtracking |
"""

class Solution:

    def generateParenthesis(self, n):
        """
        Time:  exponential in n
        Space: exponential in n
        """
        result = []

        def helper(expr, left, right):
            if len(expr) == 2 * n:
                result.append(expr)
                return
            if left < n:
                helper(expr + "(", left + 1, right)
            if right < left:
                helper(expr + ")", left, right + 1)

        helper("", 0, 0)
        return result
