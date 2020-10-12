# Problem link: https://leetcode.com/problems/reordered-power-of-2/
import math


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        """
        Returns true if any reordering (including the original) of an integer N results in a power of 2
        The reordering must not contain zeroes as leading digits
        """
        N_string = str(N)
        log2 = math.log10(2)

        min_power = math.ceil((len(N_string) - 1) / log2)
        max_power = math.floor(len(N_string) / log2)
        for p in range(min_power, max_power + 1):
            if set(str(2 ** p)) == set(N_string):
                return True
        return False
    
