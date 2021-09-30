# Problem Link: https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows <= 1):
            return s

        elif (numRows == 2):
            output1 = ""
            output2 = ""
            for i in range(len(s)):
                if (i % 2 == 0):
                    output1 += s[i]
                else:
                    output2 += s[i]
            return (output1 + output2)

        else:
            output = []
            direction = -1
            rowNumber = 0

            for i in range(numRows):
                output.append("")

            for j in range(len(s)):
                output[rowNumber] += s[j]
                if ((rowNumber == 0) or (rowNumber == numRows - 1)):
                    direction *= -1
                rowNumber += direction

            return ("".join(output))