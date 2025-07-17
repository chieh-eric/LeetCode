import bisect
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        n = len(startTime)
        job = sorted(zip(startTime,endTime,profit), key = lambda x:x[1])

        dp = [0]*n
        dp[0] = job[0][2]
        endSeq = [j[1] for j in job]
        for i in range(1,n):
            s, e, p = job[i]
            idx = bisect.bisect_right(endSeq,s) - 1

            if idx >= 0:
                dp[i] = max(dp[i-1], p+dp[idx])
            else:
                dp[i] = max(dp[i-1], p)

            
        return dp[-1]