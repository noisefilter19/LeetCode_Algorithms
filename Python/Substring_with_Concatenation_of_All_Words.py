# LeetCode Problem Link - https://leetcode.com/problems/substring-with-concatenation-of-all-words

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if (words == []) or (s == ""):
            return []
        ret_list = []
        a_word = len(words[0])
        word_lth = a_word * len(words)
        inc = 0
        words_dict = {i: words.count(i) for i in words}

        while inc <= (len(s) - word_lth):
            words_dict_cp = words_dict.copy()
            for x in range(0 + inc, word_lth + inc, a_word):
                if words_dict_cp.get(s[x: x+a_word], 0) == 0:
                    break
                else:
                    words_dict_cp[s[x: x + a_word]] -= 1
            else:
                ret_list.append(inc)
            inc += 1
        
        return ret_list
