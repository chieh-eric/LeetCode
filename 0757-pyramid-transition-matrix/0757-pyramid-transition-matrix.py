from collections import defaultdict
import heapq
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        pair = defaultdict(list)
        for allow in allowed:
            pair[allow[:2]].append(allow[2])
        
        def can_build(level):
            valid = []
            n = len(level)

            def backtrack(i,path):
                target = level[i:i+2]
                if i == n -1:
                    valid.append("".join(path[:]))
                    return
                if target not in pair:
                    return
                
                for choice in pair[target]:
                    path.append(choice)
                    backtrack(i+1,path)
                    path.pop()

            backtrack(0,[])
            return valid
        
        memo = {}
        def dfs(level):
            if len(level) == 1:
                return True
            if level in memo:
                return memo[level]

            for next_level in can_build(level):
                if dfs(next_level):
                    memo[level] = True
                    return True
            memo[level] = False
            return False
        return dfs(bottom)
                
                
                

            