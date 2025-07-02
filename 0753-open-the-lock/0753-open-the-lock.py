class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        queue = deque()
        start = "0000"
        if start not in deadends:
            queue.append((start,0))
        visited = set()
        visited.add(start)
        while queue:
            s, op = queue.popleft()
            if s == target:
                return op
            
            for i in range(4):
                for j in (1, -1):
                    new_s = s[0:i] + str((int(s[i])+j)%10) + s[i+1:]
                    if new_s not in visited and new_s not in deadends:
                        queue.append((new_s,op+1))
                        visited.add(new_s)
        return -1