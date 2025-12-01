from collections import defaultdict
class Solution(object):
    def countBlackBlocks(self, m, n, coordinates):
        """
        :type m: int
        :type n: int
        :type coordinates: List[List[int]]
        :rtype: List[int]
        """
        ans = [0]*5
        block_counts = defaultdict(int)
        for i, j in coordinates:
            if i != m - 1 and j != n - 1:
                block_counts[(i,j)] += 1

            if i - 1 >= 0 and j != n - 1:
                block_counts[(i-1,j)] += 1
            
            if j - 1 >= 0 and i != m - 1:
                block_counts[(i,j-1)] += 1
            
            if i - 1 >= 0 and j - 1 >= 0:
                block_counts[(i-1, j-1)] += 1
        #print(block_counts)
        total = len(block_counts)
        for _, val in block_counts.items():
            ans[val] += 1
        ans[0] = (m-1)*(n-1) - total
        return ans
            

