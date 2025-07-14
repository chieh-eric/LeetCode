from collections import defaultdict
class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        no_communicate = set()
        for i,j in friendships:
            if not (set(languages[i-1]) & set(languages[j-1])):
                no_communicate.add(i-1)
                no_communicate.add(j-1)
        
        min_count = float('inf')
        for i in range(1,n+1):
            count = 0
            for per in no_communicate:
                if i not in languages[per]:
                    count += 1
            min_count = min(min_count,count)
        return min_count