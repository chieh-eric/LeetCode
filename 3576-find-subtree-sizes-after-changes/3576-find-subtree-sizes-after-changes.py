from collections import defaultdict
class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        n = len(parent)
        graph = defaultdict(list)
        for i in range(1,n):
            graph[parent[i]].append(i)

        def dfs(node,track):
            if s[node] in track:
                parent[node] = track[s[node]]

            track[s[node]] = node
            for child in graph[node]:
                dfs(child,track.copy())
            return
        dfs(0,{})
        #print(parent)
        res = [1]*n
        graph = defaultdict(list)
        for i in range(1,n):
            graph[parent[i]].append(i)
        def count(node):
            if node not in graph:
                return 1
            
            for child in graph[node]:
                res[node] += count(child)
            return res[node]
        #print(graph)
        #print(parent)
        count(0)
        return res
                    