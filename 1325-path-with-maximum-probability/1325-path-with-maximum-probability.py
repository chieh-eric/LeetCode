from collections import defaultdict
class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        graph = defaultdict(list)
        for index,(i, j) in enumerate(edges):
            graph[i].append((succProb[index], j))
            graph[j].append((succProb[index], i))
        
        queue = deque()
        queue.append((1,start_node))
        count = defaultdict(int)

        while queue:
            prob, node = queue.popleft()

            for route_prob, neighbor in graph[node]:
                if count[neighbor] < prob * route_prob:
                    count[neighbor] = prob * route_prob
                    queue.append((count[neighbor],neighbor))
        return count[end_node]
        