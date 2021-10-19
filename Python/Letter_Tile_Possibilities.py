class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = collections.Counter(tiles)
        product = 1
        for f in freq.values():
            product *= f + 1
        counter = 0
        for i in range(1, product):
            digits = []
            for f in freq.values():
                digits.append(i % (f + 1))
                i = i // (f + 1)
            tmp = math.factorial(sum(digits))
            for d in digits:
                tmp //= math.factorial(d)
            counter += tmp
        return counter
