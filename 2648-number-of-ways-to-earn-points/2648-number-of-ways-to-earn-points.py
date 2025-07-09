class Solution(object):
    def waysToReachTarget(self, target, types):
        """
        :type target: int
        :type types: List[List[int]]
        :rtype: int
        """
        # dp[i][points] be the number of way until types i and possible points
        # Recursive form: dp[i][points] = dp[i-1][points-mark[i]*c] over 0 <= c <= count 
        n = len(types)
        dp = [[0]*(target+1) for _ in range(n)]
        # Initialize
        mod = 10**9 +7
        count1 = types[0][0]
        mark1 = types[0][1]
        dp[0][0] = 1
        for i in range(1, count1 + 1):
            if i * mark1 <= target:
                dp[0][i * mark1] = 1

        #print(dp)
        for i in range(1,n):
            count = types[i][0]
            mark = types[i][1]
            for score in range(target+1):

                for k in range(count+1):
                    if score-k*mark >= 0:
                        dp[i][score] += dp[i-1][score-k*mark] 
                        dp[i][score] %= mod
                    else:
                        break
        #print(dp)
        return dp[n-1][target]
            
            
