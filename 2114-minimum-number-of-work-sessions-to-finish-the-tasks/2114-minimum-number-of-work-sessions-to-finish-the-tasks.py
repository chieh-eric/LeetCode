class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        n = len(tasks)
        dp = [[float('inf')]*(sessionTime+1) for _ in range(2**n)]
        dp[0][0] = 1

        for mask in range(2**n):
            for time in range(sessionTime+1):
                if dp[mask][time] == float('inf'):
                    continue
                
                for i in range(n):
                    if (mask>>i) & 1:
                        continue
                    
                    new_mask = mask | (1<<i)
                    task_time = tasks[i]

                    if time + task_time > sessionTime:
                        dp[new_mask][task_time] = min(dp[new_mask][task_time], dp[mask][time] + 1)
                    else:
                        dp[new_mask][task_time+time] = min(dp[new_mask][task_time+time],dp[mask][time])
        final_statue = (1 << n) -1
        return min(dp[final_statue])