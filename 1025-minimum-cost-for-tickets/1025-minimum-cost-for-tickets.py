class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [float('inf')]*(days[-1]+1)
        dp[0] = 0
        set_days = set(days)
        for i in range(1,days[-1]+1):
            if i in set_days:
                # 1-day
                dp[i] = min(dp[i],dp[i-1]+costs[0])
                # 7-day
                if i >= 7:
                    dp[i] = min(dp[i],dp[i-7]+costs[1])
                else:
                    dp[i] = min(dp[i],dp[0]+costs[1])
                # 30-day
                if i >= 30:
                    dp[i] = min(dp[i],dp[i-30]+costs[2])
                else:
                    dp[i] = min(dp[i],dp[0]+costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[-1]