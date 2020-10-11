"""
Topics: | None |
"""

class Solution:

    def licenseKeyFormatting(self, S, K):
        """
        Time:  O(n)
        Space: O(n)
        """
        S = S.upper().replace('-', '')

        N = len(S)
        i = K if N % K == 0 else N % K

        result = []
        result.append(S[:i])
        while i < N:
            result.append('-')
            result.append(S[i : i+K])
            i += K

        return ''.join(result)
