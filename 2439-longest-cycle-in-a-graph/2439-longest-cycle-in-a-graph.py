class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        graph = {}
        for i, to in enumerate(edges):
            if to != -1:
                graph[i] = to
        n = len(edges)
        self.max_length = -1

        stepMap = {}
        def dfs(node,step):
            if node in stepMap:
                if start_node == stepMap[node][1]:
                    self.max_length = max(self.max_length, step - stepMap[node][0])
                return
            if node in visited:
                return
            visited.add(node)
            stepMap[node] = (step, start_node) 
            if node in graph:
                dfs(graph[node],step+1)

        visited = set()
        for i in range(n):
            if i not in visited:
                start_node = i
                dfs(i,0)
        return self.max_length

        #0 -> 1 -> 2 -> 0

        #3 -> 4 ->5 -> 6 -> 3

        #7 -> 8 -> 9 -> 7