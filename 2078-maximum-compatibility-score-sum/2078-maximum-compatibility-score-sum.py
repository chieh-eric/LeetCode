class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        n = len(students)

        scores = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                scores[i][j] = sum(mentors[j][k] == students[i][k] for k in range(len(students[i])))
        #print(scores)
        def dp(i, mask):
            if i == n:
                return 0
            
            res = 0
            for j in range(n):
                b = 2**j
                if mask // b % 2 > 0:
                    res = max(res, scores[i][j] + dp(i+1,mask-b))
            return res
        



        return dp(0,2**(n)-1)
       