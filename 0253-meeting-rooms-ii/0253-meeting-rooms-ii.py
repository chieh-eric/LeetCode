class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # (0, +1),  (5, +1), (10, -1), (15, +1), (20, -1), (30, -1)  
        times = []
        for start, end in intervals:
            times.append((start,1))
            times.append((end, -1))
        times.sort(key=lambda x:(x[0], x[1]))
        cur = 0
        ans = 0
        for _, var in times:
            cur += var
            ans = max(ans, cur)
        return ans


        