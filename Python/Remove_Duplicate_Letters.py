class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        countMap = collections.defaultdict(int)
        stack = []
        visited = set()

        for c in s:
            countMap[c] += 1

        for ch in s:
            countMap[ch] -= 1
            if ch not in visited:
                while stack and countMap[stack[-1]] > 0 and stack[-1] > ch:
                    visited.remove(stack.pop())
                    
                stack.append(ch)
                visited.add(ch)
                
        return "".join(stack)
