class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        events = []
        for interval in intervals:
            arrive = interval[0]
            leave = interval[1]
            events.append((arrive,1))
            events.append((leave,-1))
        events.sort(key=lambda x:(x[0],-x[1]))
        group = cur = 0
        for event in events:
            cur += event[1]
            group = max(group,cur)
        return group