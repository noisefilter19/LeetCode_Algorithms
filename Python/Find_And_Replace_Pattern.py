class Solution:
    def get_num_word(self, word: str):
        num = ''
        alphabets = [None] * 26
        for i, letter in enumerate(word):
            position = ord(letter) - 97
            if alphabets[position] == None:
                alphabets[position] = i
                num += str(i)
            else:
                num += str(alphabets[position])
        return num
            
    def findAndReplacePattern(self, words, pattern: str):
        numPattern = self.get_num_word(pattern)
        matched = []
        for word in words:
            numWord = self.get_num_word(word)
            if numPattern == numWord:
                matched.append(word)
        return matched