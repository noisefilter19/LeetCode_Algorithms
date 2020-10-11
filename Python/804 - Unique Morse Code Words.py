"""
Topics: | String |
"""

class Solution:
    """
    Time:  O(s)  [s = sum of lengths of all words in 'words']
    Space: O(s)
    """

    def uniqueMorseRepresentations(self, words):
        morse_encodings = {self.english_to_morse(word) for word in words}
        return len(morse_encodings)

    def english_to_morse(self, word):
        morse = [self.MORSE_MAPPINGS[c] for c in word]
        return ''.join(morse)

    MORSE_MAPPINGS = {
        'a':  '.-',
        'b':  '-...',
        'c':  '-.-.',
        'd':  '-..',
        'e':  '.',
        'f':  '..-.',
        'g':  '--.',
        'h':  '....',
        'i':  '..',
        'j':  '.---',
        'k':  '-.-',
        'l':  '.-..',
        'm':  '--',
        'n':  '-.',
        'o':  '---',
        'p':  '.--.',
        'q':  '--.-',
        'r':  '.-.',
        's':  '...',
        't':  '-',
        'u':  '..-',
        'v':  '...-',
        'w':  '.--',
        'x':  '-..-',
        'y':  '-.--',
        'z':  '--..',
    }
