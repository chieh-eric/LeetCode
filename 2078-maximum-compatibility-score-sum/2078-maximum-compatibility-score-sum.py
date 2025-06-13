from itertools import permutations
class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        def score(s,m):
            return sum(x==y for x, y in zip(s,m))
        max_score = 0
        n = len(students)
        for perm in permutations((range(n))):
            total = 0
            for i in range(n):
                total += score(students[i],mentors[perm[i]])
            max_score = max(max_score,total)
        return max_score

