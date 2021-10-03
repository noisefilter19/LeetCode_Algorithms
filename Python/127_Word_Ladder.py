# 127 Word Ladder - Hard - https://leetcode.com/problems/word-ladder/

from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                s = word[:i]+'_'+word[i+1:]
                graph[s].append(word)
                    
        dq = deque([beginWord])
           
        visited = set(beginWord)
        path = 0
        while dq:
            path += 1
            for _ in range(len(dq)):
                word = dq.popleft()
                if word == endWord:
                    return path
                
                for i in range(len(word)):
                    s = word[:i]+'_'+word[i+1:]
                    for child in graph[s]:
                        if child not in visited:
                            visited.add(child)
                            dq.append(child)

        return 0
