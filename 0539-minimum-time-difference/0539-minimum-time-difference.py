class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        transform = []
        for time in timePoints:
            split = time.split(":")
            hr = int(split[0])
            m = int(split[1])
            transform.append(hr*60+m)
        transform.sort()
        transform.append(1440+transform[0])
        n = len(transform)
        min_diff = float('inf')
        for i in range(1,n):
            min_diff = min(min_diff, transform[i] - transform[i-1])
        return min_diff
       # print(transform)