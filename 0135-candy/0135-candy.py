class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        left = [1]*n
        right = [1]*n
        
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                left[i] += left[i-1]
        #print(left)

        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                right[i] += right[i+1]
        #print(right)
        # 1 2 3 3 2 1 2 3
        # 1 2 3 4 3 2 1 2 3 2 1
        return sum(max(right[i],left[i]) for i in range(n))