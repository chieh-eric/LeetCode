from collections import defaultdict
class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # Build the graph
        # Use BFS, queue(cur_node, numOddPath, numEvenPath, depth)
        # queue(1,0,0,0) -> (2,1,1,1), (3,1,1,1) -> (4,2,2,2) -> (5,2,2,2) 
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()
        queue = deque()
        queue.append((1,0,0,0))
        max_depth = 0
        max_odd = 0
        mod = 10**9 + 7
        while queue:
            node, numOdd, numEven, depth = queue.popleft()
            visited.add(node)
            if depth > max_depth:
                max_depth = depth
                max_odd = numOdd

            for nei in graph[node]:
                if nei not in visited:
                    if numOdd == 0 and numEven == 0:
                        queue.append((nei, 1, 1, depth + 1))
                    else:
                        queue.append((nei, numEven + numOdd, numOdd + numEven, depth + 1))

        return max_odd % mod

        # 1
        # 2
        # 3
        # 4
