from collections import defaultdict
class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        # Build graph -> x, y, r
        # dfs -> return number of bombs will exploded (Memorization)

        def calculation(i, j):
            sx, sy, sr = bombs[i]
            ex, ey, _ = bombs[j]
            return abs(sx-ex)**2 + abs(sy-ey)**2 <= sr**2
        
        graph = defaultdict(list)
        n = len(bombs)
        for i in range(n-1):
            for j in range(i+1, n):
                if calculation(i,j):
                    graph[i].append(j)
                if calculation(j,i):
                    graph[j].append(i)   
             
    
        memo = {}
        def dfs(index, path):
            #if index in memo:
                #return memo[index]

            path.add(index)
            count = 1
            for nei in graph[index]:
                if nei not in path:
                    count += dfs(nei, path)
            #memo[index] = count
            return count
        
        
        max_count = 0
        for i in range(n):
            #visited = set()
            max_count = max(max_count, dfs(i, set()))
        #print(memo)
        return max_count
