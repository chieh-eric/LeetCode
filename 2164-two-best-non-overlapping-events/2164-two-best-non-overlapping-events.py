import bisect
class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort(key=lambda x:(x[1],-x[2]))
        #print(events)

        max_value = []
        cur = 0
        for _, end, value in events:
            cur = max(cur,value)
            max_value.append((end,cur))
        #print(max_value)
        ends = [end for _, end, _ in events]
        res = 0
        for start, end, value in events:
            idx = bisect.bisect_right(ends, start - 1) - 1
            if idx >= 0:
                res = max(res, max_value[idx][1] + value)
            else:
                res = max(res, value)

        return res