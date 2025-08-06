from collections import defaultdict
class Solution(object):
    def maximumScore(self, scores, edges):
        """
        :type scores: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(scores)
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        top_neighbor = defaultdict(list)
        for i in range(n):
            graph[i].sort(key = lambda x:-scores[x])
            top_neighbor[i] = graph[i][:3]
            
        #print(top_neighbor)
        max_score = -1
        for u, v in edges:
            for x in top_neighbor[u]:
                if x == v:
                    continue
                for y in top_neighbor[v]:
                    if u == y or x == y:
                        continue
                    max_score = max(max_score ,scores[x]+scores[u]+scores[v]+scores[y])
        return max_score