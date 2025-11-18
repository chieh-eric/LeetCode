class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        #print(intervals)
        res = [intervals[0]]
        n = len(intervals)
        i = 1
        while i < n:
            start, end = intervals[i]
            smallest_end = res[-1][1]
            if start <= smallest_end:
                res[-1][1] = max(smallest_end, end)
            else:
                res.append([start,end])
            i += 1
            
        #print(res)
        return res