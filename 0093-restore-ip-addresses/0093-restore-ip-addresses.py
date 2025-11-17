class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n > 12 or n < 4:
            return []
        # DFS(i,j,d)

        ans = []
        # index -> Start point
        # d -> Remaining devision
        visited = set()
        def dfs(start, d, path):
            if d == 0 and start == n:
                if len(path) == 4 and tuple(path) not in visited:
                    #print(path[::])
                    visited.add(tuple(path))
                    ans.append(path[::])
                return
            if start == n:
                return

            for i in range(1,4):
                end = start + i
                max_distance = min(end, n)
                #print(start, max_distance)
                if int(s[start:max_distance]) <= 255:
                    if s[start] == "0" and i > 1:
                        continue
                    path.append(s[start:max_distance])
                    dfs(max_distance, d - 1, path)
                    path.pop()

        dfs(0,4,[])
        #print(ans)
        ret = []
        for element in ans:
            ret.append(".".join(element))
        return ret
            

            
                


        