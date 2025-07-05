import bisect 
class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort(key=lambda x:(x[1]))
        n = len(events)
        max_value_up_to = []
        cur_max = 0
        for start, end, val in events:
            cur_max = max(cur_max, val)
            max_value_up_to.append((end,cur_max))
        max_val = 0
        ends = [end for _, end, _ in events]
        for i in range(n):
            cur = events[i][2]
            start = events[i][0]
            idx = bisect.bisect_right(ends, start - 1) - 1 
            if idx == -1:
                max_val = max(max_val, cur)
                continue
            
            cur += max_value_up_to[idx][1]
            max_val = max(max_val, cur)
        return max_val