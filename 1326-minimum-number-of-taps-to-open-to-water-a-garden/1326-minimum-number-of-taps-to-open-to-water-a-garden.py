class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        # [(0,3),(1,3),(2,4),(0,5)]
        # while loop, start vairalbe, find a range that cover this start position

        m = len(ranges)
        intervals = []
        for i, val in enumerate(ranges):
            # if val == 0:
            #     continue
            intervals.append((max(0, i - val), min(n, i + val)))

        intervals.sort()

        start = 0
        count = 0
        i = 0
        #print(intervals)
        while start < n and i < len(intervals):

            best = start
            while i < len(intervals) and start >= intervals[i][0]:
                best = max(best, intervals[i][1])
                i += 1
            
            if best == start:
                return -1
            
            start = best
            count += 1
        return count
            



        