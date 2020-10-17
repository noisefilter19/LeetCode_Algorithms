#https://leetcode.com/problems/sort-characters-by-frequency/
class Solution:
    def sort_characters_by_frequency(self, s: str) -> str:
        if s == '': return ''
        freq = {}
        for each in s:
            if each not in freq:
                freq[each] = 1
            else:
                freq[each] += 1
        sorted_freq = dict(sorted(freq.items(),key = lambda item:item[1],reverse = True))
        res = ''
        for key,val in sorted_freq.items():
            res += key * val
        return res