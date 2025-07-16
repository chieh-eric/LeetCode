class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        visited = set()
        queue = deque()
        queue.append(s)
        res = s
        n = len(s)
        while queue:
            val = queue.popleft()
            res = min(res,val)
            added = list(val)
            for i in range(1,n,2):
                added[i] = str((int(added[i])+a) %10)
            added = "".join(added)
            if added not in visited:
                queue.append(added)
                visited.add(added)
            
            rotated = val[-b:] + val[:-b]
            if rotated not in visited:
                queue.append(rotated)
                visited.add(rotated)
        return res