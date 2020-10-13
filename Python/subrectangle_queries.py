
# link: https://leetcode.com/problems/subrectangle-queries/

class SubrectangleQueries:

    def __init__(self, lists):
        self.rectangle = lists

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for i in range(col1, col2 + 1):
            for j in range(row1, row2 + 1):
                self.rectangle[j][i] = newValue

    def getValue(self, row, col):
        return self.rectangle[row][col]

