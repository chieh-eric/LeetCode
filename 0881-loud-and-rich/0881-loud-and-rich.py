from collections import defaultdict
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        indegree = defaultdict(int)
        quiet_index = {}
        
        for r, p in richer:
            graph[r].append(p)
            indegree[p] += 1
        
        n = len(quiet)
        ans = [0]*n
        queue = deque()
        for i in range(n):
            if i not in indegree:
                queue.append(i)
            quiet_index[i] = (quiet[i], i)
        
        while queue:
            node = queue.popleft()
            ans[node] = quiet_index[node][1]

            for child in graph[node]:
                indegree[child] -= 1
                if quiet_index[node][0] < quiet_index[child][0]:
                    quiet_index[child] = quiet_index[node]
                if indegree[child] == 0:
                    queue.append(child)
        #print(richer_list)
        return ans
            

                
        

        
        