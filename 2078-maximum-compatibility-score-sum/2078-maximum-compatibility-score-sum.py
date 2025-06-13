class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        # Use DP with bitmap
        # Initial Case: dp[mask] -> mask means the selected mentor
        n = len(students)
        dp = [0]* (1<<n)

        # Prepare the student-mentors score pairs
        score = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                score[i][j] = sum(a==b for a,b in zip(students[i],mentors[j]))
        
        for mask in range(1<<n):
            i = bin(mask).count('1')

            if i >= n:
                continue
            
            for j in range(n):
                if not (mask >> j) & 1:
                    new_mask = mask | 1<<j
                    dp[new_mask] = max(dp[new_mask],dp[mask]+score[i][j])
        return dp[(1<<n)-1]


