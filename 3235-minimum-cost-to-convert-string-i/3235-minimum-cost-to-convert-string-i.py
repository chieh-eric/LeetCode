from collections import defaultdict
import heapq
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        dist = [[float('inf')]*26 for _ in range(26)]

        for i in range(26):
            dist[i][i] = 0
        
        for i in range(len(original)):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            dist[u][v] = min(dist[u][v], cost[i])
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        cost = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                u = ord(source[i]) - ord('a')
                v = ord(target[i]) - ord('a')
                if dist[u][v] == float('inf'):
                    return -1
                cost += dist[u][v]
        return cost