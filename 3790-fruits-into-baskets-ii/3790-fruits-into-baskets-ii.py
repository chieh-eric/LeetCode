class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        count = 0
        i = 0
        n = len(fruits)
        m = len(baskets)
        occupy = [False]*m

        for i in range(n):
            
            for j in range(m):
                if fruits[i] <= baskets[j] and not occupy[j]:
                    occupy[j] = True
                    count += 1
                    break
        return n - count