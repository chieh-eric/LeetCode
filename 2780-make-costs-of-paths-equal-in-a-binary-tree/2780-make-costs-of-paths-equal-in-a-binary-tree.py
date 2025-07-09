class Solution(object):
    def minIncrements(self, n, cost):
        """
        :type n: int
        :type cost: List[int]
        :rtype: int
        """
        l = len(cost)
        self.max_path = 0
        self.count = 0

        def dfs(i,cur):
            cur += cost[i-1]
            if 2*i > l and 2*i + 1 > l:
                self.max_path = max(self.max_path,cur)
                return
            
            dfs(2*i,cur)
            dfs(2*i+1,cur)

        dfs(1,0)

        def find(i,cur):
            cur += cost[i-1]
            if 2*i > l and 2*i + 1 > l:
                return self.max_path - cur
            
            left = find(2*i,cur)
            right = find(2*i+1,cur)
            min_val = min(left,right)
            self.count += (left+right) - 2*min_val
            return min_val
                                                  
        find(1,0)
        #print(self.max_path)
        #print(self.count)
        return self.count