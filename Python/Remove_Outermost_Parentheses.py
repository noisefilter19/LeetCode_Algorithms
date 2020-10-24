class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        primitives = []
        parentheses = 0

        temp = []
        for parenthesis in S:
            temp.append(parenthesis)
            if parenthesis == '(':
                parentheses += 1
            elif parenthesis == ')':
                parentheses -= 1

            if parentheses == 0:
                primitives.append(''.join(temp))
                temp = []

        return ''.join([x[1:-1] for x in primitives])
        