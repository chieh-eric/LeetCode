from itertools import permutations
class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """

        max_score = 0
        n = len(students)
        m = len(students[0])
        for perm in permutations(students):
            s = 0
            for i in range(n):
                s += sum(perm[i][j] == mentors[i][j] for j in range(m))
            max_score = max(max_score,s)
        return max_score
             
