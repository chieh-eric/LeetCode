from collections import defaultdict
class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        ans = [0]* n
        def dfs(fr, node):
            
            dic = defaultdict(int)
            if len(graph[node]) == 1 and graph[node][0] == fr:
                dic[labels[node]] = 1
                ans[node] = 1
                return dic

            for neighbor in graph[node]:
                if neighbor != fr:
                    child_counter = dfs(node,neighbor)
                    for key, value in child_counter.items():
                        dic[key] += value

            dic[labels[node]] = dic.get(labels[node],0) + 1
            ans[node] = dic[labels[node]]
            return dic
        dfs(None,0)
        return ans
                