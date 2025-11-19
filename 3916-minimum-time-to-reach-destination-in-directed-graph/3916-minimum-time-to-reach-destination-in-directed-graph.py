from collections import defaultdict
import heapq
class Solution(object):
    def minTime(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        queue = []
        queue.append((0,0))

        for start_pos, end_pos, start_t, end_t in edges:
            graph[start_pos].append((end_pos,start_t,end_t))
        
        visited = set()

        while queue:
            time, node = heapq.heappop(queue)
            if node in visited:
                continue
            if node == n - 1:
                return time

            visited.add(node)
            for nei, start_t, end_t in graph[node]:
                if time > end_t or nei in visited:
                    continue
                elif time >= start_t:
                    heapq.heappush(queue,(time+1, nei))
                else:
                    heapq.heappush(queue,(start_t+1, nei))

        return -1

        