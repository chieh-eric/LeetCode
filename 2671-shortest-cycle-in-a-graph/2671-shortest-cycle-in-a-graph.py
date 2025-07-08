from collections import defaultdict
class Solution(object):
    def findShortestCycle(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        min_val = float('inf')    
        for start in range(n):
            queue = deque()
            queue.append((start,-1,0))
            visited = {start:0}

            while queue:
                node, parent, step = queue.popleft()
                
                for neighbor in graph[node]:
                    if neighbor == parent:
                        continue
                    if neighbor in visited:
                        cy_len = step + visited[neighbor] + 1
                        min_val = min(min_val,cy_len)
                    else:
                        visited[neighbor] = step + 1
                        queue.append((neighbor, node, step+1))

        return min_val if min_val != float('inf') else -1

        # 0 -> 1 -> 2 -> 3 -> 4 -> 5 
        # 0 -> 7 -> 5 -> 6 -> 0
