from collections import defaultdict
import heapq
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        n = len(original)
        for i in range(n):
            graph[original[i]].append((cost[i],changed[i]))

        transform ={}
        m = len(source)
        def calculate(s1,s2):
            queue = []
            queue = [(0,s1)]
            visited = set()
            visited.add(s1)

            while queue:
                cur_cost, ch = heapq.heappop(queue)
                
                if ch == s2:
                    
                    return cur_cost
                visited.add(ch)

               
                for nei in graph[ch]:
                    if nei[1] not in visited:
                        heapq.heappush(queue,(cur_cost+nei[0],nei[1]))
            return -1

        cost = 0
        for i in range(m):
            if source[i] != target[i]:
                if (source[i],target[i]) in transform:
                    cost += transform[(source[i],target[i])]
                else:
                    res = calculate(source[i],target[i])
                    if res == -1:
                        return -1
                    cost += res
                    transform[(source[i],target[i])] = res
        return cost
        