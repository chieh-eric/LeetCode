from itertools import permutations
class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        def score(s, m):
            return sum(x == y for x, y in zip(s, m))

        m = len(students)
        best = 0
        for perm in permutations(range(m)):
            total = sum(score(students[i], mentors[perm[i]]) for i in range(m))
            best = max(best, total)
        return best


