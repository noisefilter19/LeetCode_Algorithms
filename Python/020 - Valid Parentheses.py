"""
Topics: | String | Stack |
"""

class Solution:

    def isValid(self, string):
        """
        Time:  O(n)
        Space: O(n)  [worst case: only opening brackets]
        """
        brackets = { '(': ')',
                     '[': ']',
                     '{': '}', }

        stack = []
        for ch in string:
            if ch in brackets.keys():
                stack.append(ch)
            elif ch in brackets.values():
                if not stack:
                    return False
                elif brackets[stack.pop()] != ch:
                    return False
            else:
                return False
        return not stack  # Non-empty stack => unbalanced brackets
