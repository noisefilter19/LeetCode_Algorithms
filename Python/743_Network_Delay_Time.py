# https://leetcode.com/problems/network-delay-time/

from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        self.graph = [deque() for i in range(N+1)]
        for u, v, w in times:
            self.graph[u].append((v, w))

        self.dist = [float('inf')] * (N+1)
        self.dfs(K)
        tot = max(self.dist[1:])
        return tot if tot != float('inf') else -1
    
    def dfs(self, v, elapsed=0):
        if elapsed >= self.dist[v]: return
        
        self.dist[v] = elapsed
        for neighbor, weight in self.graph[v]:
            self.dfs(neighbor, elapsed + weight)
