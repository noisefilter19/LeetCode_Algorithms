"""
Topics: | Array |
"""

class Solution:

    # Using only one row
    def getRow(self, row_index):
        """
        Time:  O(n^2)
        Space: O(n)

        [n = row_index]
        """
        row = [1] * (row_index + 1)
        for i in range(1, row_index):
            for j in reversed(range(1, i + 1)):
                row[j] += row[j - 1]
        return row

#     # Using two rows (optimized DP)
#     def getRow(self, row_index):
#         """
#         Time:  O(n^2)
#         Space: O(n)
#
#         [n = row_index]
#         """
#         curr_row = [1]
#         for k in range(1, row_index + 1):
#             prev_row = curr_row
#             curr_row = [1] * (k + 1)
#             for i in range(1, k):
#                 curr_row[i] = prev_row[i - 1] + prev_row[i]
#         return curr_row
