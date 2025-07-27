class Solution(object):
    def minmaxGasDist(self, stations, k):
        """
        :type stations: List[int]
        :type k: int
        :rtype: float
        """
        n = len(stations)
        left = 1e-6
        right = stations[-1] - stations[0]

        while left + 1e-6 < right:
            mid = (left+right) / 2
            count = 0
            for i in range(1,n):
                count += math.ceil((stations[i]-stations[i-1])/mid) - 1
            if count > k:
                left = mid 
            else:
                right = mid
        return left