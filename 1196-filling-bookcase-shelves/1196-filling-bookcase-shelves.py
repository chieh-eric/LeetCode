class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        # dp[i] means the minumum height after order 0 ~ i-1 (index) books
        # Transition form: 
        n = len(books)
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        
        for i in range(n+1):
            width  = 0
            height = 0
            for j in range(i,0,-1):
                width += books[j-1][0]
                if width > shelfWidth:
                    break
                height = max(height,books[j-1][1])
                dp[i] = min(dp[i],dp[j-1]+height)
        return dp[n]