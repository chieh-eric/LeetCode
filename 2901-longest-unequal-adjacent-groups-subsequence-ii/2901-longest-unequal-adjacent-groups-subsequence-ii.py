from collections import defaultdict
class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        # Use dictionary with key as lenght, value as list of words
        # Use two for loop to calucalte the restriction
        # Use graph logic, if pass two restrictions, assign an edge from the smaller index to the larger
        n = len(words)
        dp = [1]*n
        parent = [-1]*n
        maxi = 1

        def check(i, j):
            word1 = words[i]
            word2 = words[j]
            if len(word1) != len(word2):
                return False
            if groups[i] == groups[j]:
                return False
            diffCount = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    diffCount += 1
            return diffCount == 1
        
        for i in range(n):
            for j in range(i):
                if check(i,j) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                if dp[i] > maxi:
                    maxi = dp[i]
        
        res = []
        for i in range(n):
            if dp[i] == maxi:
                while i != -1:
                    res.append(words[i])
                    i = parent[i]
                break
        return res[::-1]
        