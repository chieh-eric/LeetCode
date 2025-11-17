from collections import defaultdict
class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        # Build graph -> x, y, r
        # dfs -> return number of bombs will exploded (Memorization)

        # graph = defaultdict(list)
        # for x, y, r in bombs:
        #     graph
    
        #memo = {}
        n = len(bombs)
        def dfs(index, path):
            #if index in memo:
             #   return memo[index]

            path.add(index)
            x, y, r = bombs[index]
            count = 1
            for i in range(n):
                if i == index:
                    continue
                nei_x, nei_y, _ = bombs[i]
                if (nei_x - x)**2 + (nei_y - y)**2 <= r**2 and  i not in path:
                    count = count + dfs(i, path)
            #memo[index] = count
            return count
        
        
        max_count = 0
        for i in range(n):
            #visited = set()
            max_count = max(max_count, dfs(i, set()))
        #print(memo)
        return max_count
