from collections import defaultdict
class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        if len(edges) == 0:
            return 1
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        queue = deque()
        queue.append((1,1,t))
        visited = set()
        visited.add(1)

        leaves = set()
        for node in graph:
            if node != 1 and len(graph[node]) == 1:
                leaves.add(node)

        while queue:
            node, prob, time = queue.popleft()
            n = len(graph[node])
            child_num = n - 1 if node != 1 else n
            if node == target and (time == 0 or (node in leaves and time > 0)):
                return prob
            visited.add(node)
            for child in graph[node]:
                if child != node and child_num != 0 and child not in visited:
                    queue.append((child,(float(prob)/child_num),time-1))
        return 0

        #  1
        # 2       
        # 3   
        # 4  5   7      
        # 8  6 9
