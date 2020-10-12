# Problem link: https://leetcode.com/problems/count-number-of-teams/

import itertools
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i,j,k in itertools.combinations(rating,3):
            if i>j>k or i<j<k:
                count+=1
        return count