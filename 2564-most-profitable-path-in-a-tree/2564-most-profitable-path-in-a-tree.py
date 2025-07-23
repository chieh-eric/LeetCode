from collections import defaultdict
class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        queue = deque()
        
        path = []
        def dfs(node, parent):
            if node == 0:
                path.append(node)
                return True

            for nei in graph[node]:
                if nei == parent:
                    continue
                if dfs(nei,node):
                    path.append(node)
                    return True
            return False
        dfs(bob,None)
        path = path[::-1]
        share = set()
        m = len(path) 
        if m % 2:
            share.add(path[m//2])
        no_price = set()
        for i in range(m//2):
            no_price.add(path[i])
       

        self.max_profit = -float('inf')

        def find(node,parent,profit):

            count = amount[node]
            if node in no_price:
                count = 0
            
            if node in share:
                count //= 2

            if len(graph[node]) == 1 and node != 0:
                ##print(node)
                self.max_profit = max(self.max_profit, profit + count)

            for nei in graph[node]:
                if nei == parent:
                    continue
                find(nei,node, profit+count)
        find(0,None,0)
        return self.max_profit