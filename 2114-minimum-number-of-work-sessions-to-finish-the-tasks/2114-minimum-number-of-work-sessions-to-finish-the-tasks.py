from collections import defaultdict
class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        n = len(tasks)
        dp = defaultdict(dict)
        dp[0][0] = 1

        for mask in range(2**n):
            for time in dp[mask]:
                session = dp[mask][time]
                
                for i in range(n):
                    if (mask>>i) & 1:
                        continue
                    
                    new_mask = mask | (1<<i)
                    task_time = tasks[i]

                    if time + task_time > sessionTime:
                        if task_time not in dp[new_mask] or dp[new_mask][task_time] > session + 1:
                            dp[new_mask][task_time] = session + 1
                    else:
                        if task_time+time not in dp[new_mask]:
                            dp[new_mask][task_time+time] = session
        final_statue = (1 << n) -1
        return min(dp[final_statue].values())