class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        n = len(edges)
        visited = [0]*n
        self.max_len = -1

        def dfs(node, step):
            if node == -1:
                return 
            if visited[node] == -1:
                return

            if visited[node] != 0:
                self.max_len = max(self.max_len, step - visited[node])
                return
            
            visited[node] = step
            dfs(edges[node], step + 1)
            visited[node] = -1

        for i in range(n):
            if visited[i] != -1:
                dfs(i,0)
        return self.max_len