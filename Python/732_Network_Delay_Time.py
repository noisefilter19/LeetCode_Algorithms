# Network Delay Time
# Problem link: https://leetcode.com/problems/network-delay-time/
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float('inf')]*N
        dist[K-1] = 0

        for _ in range(N):
            for time in times:
                u, v, w = time
                dist[v-1] = min(dist[v-1], dist[u-1]+w)
        max_dist = max(dist)
        return -1 if max_dist == float('inf') else max_dist
