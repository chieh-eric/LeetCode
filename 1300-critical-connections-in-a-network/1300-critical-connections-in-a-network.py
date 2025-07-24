from collections import defaultdict
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)

        disc = [-1]*n
        low = [-1]*n
        res = []
        time = [0]

        def dfs(node,parent):
            disc[node] = low[node] = time[0]
            time[0] += 1

            for nei in graph[node]:
                if nei == parent:
                    continue

                if disc[nei] == -1:
                    dfs(nei,node)
                    low[node] = min(low[node],low[nei])
                    if low[nei] > disc[node]:
                        res.append((nei,node))

                else:
                    low[node] = min(low[node],disc[nei])
        dfs(0,None)
        return res