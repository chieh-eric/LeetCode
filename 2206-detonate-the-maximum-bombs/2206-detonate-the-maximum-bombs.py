from collections import defaultdict
class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        n = len(bombs)
        distance = {}

        def calculate(s1,s2):
            way = 0
            x1, y1, r1 = s1[0], s1[1], s1[2]
            x2, y2, r2 = s2[0], s2[1], s2[2]
            if (x1,y1,x2,y2) in distance:
                way= distance[(x1,y1,x2,y2)]
            else:
                way = ((x1-x2)**2 + (y1-y2)**2)**0.5
                distance[(x1,y1,x2,y2)] = way
                distance[(x2,y2,x1,y1)] = way
            if way <= r1:
                return True
            return False

            
        for i in range(n):
            for j in range(n):
                if i != j:
                    if calculate(bombs[i],bombs[j]):
                        graph[i].append(j)
        
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            found = 1
            if graph[node]:
                for nei in graph[node]:
                    if nei not in visited:
                        ans = dfs(nei)
                        found += ans
            return found

        max_length = 0
        for i in range(n):
            visited = set()
            res = dfs(i)
            max_length = max(max_length,res)
        return max_length
