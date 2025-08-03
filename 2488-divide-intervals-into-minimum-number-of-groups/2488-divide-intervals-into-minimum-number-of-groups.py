class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        events = []
        for i, j in intervals:
            events.append((i,1))
            events.append((j,-1))
        cur = group = 0
        events.sort(key=lambda x:(x[0],-x[1]))
        for _, i in events:
            cur += i
            group = max(group, cur)
        return group