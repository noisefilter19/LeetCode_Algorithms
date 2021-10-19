"""
Link : https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

1579. Remove Max Number of Edges to Keep Graph Fully Traversable (Hard)

Alice and Bob have an undirected graph of n nodes and 3 types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can by traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if it's impossible for the graph to be fully traversed by Alice and Bob.
"""

class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        return True
    
    def size(self, x):
        return self.sz[self.find(x)]

class Solution:
    def maxNumEdgesToRemove(self, n: int, a: List[List[int]]) -> int:
        dsu1, dsu2 = DSU(n), DSU(n)
        d = {}
        
        for t, x, y in a:
            x -= 1
            y -= 1
            if t in d:
                d[t].append([x, y])
            else:
                d[t] = [[x,y]]
                
        ans = 0
        
        if 3 in d:
            for i in d[3]:
                x, y = i
                dsu2.union(x, y)
                if not dsu1.union(x, y):
                    ans += 1
        
        if 1 in d:
            for i in d[1]:
                x, y = i
                if not dsu1.union(x, y):
                    ans += 1
                
        if 2 in d:
            for i in d[2]:
                x, y = i
                if not dsu2.union(x, y):
                    ans += 1
        
        if dsu1.size(0) != n or dsu2.size(0) != n:
            return -1
        return ans