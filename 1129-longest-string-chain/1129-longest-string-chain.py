class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        m = len(words)
        words.sort(key=lambda x:len(x))
        def calculate(source,target):
            if len(source) + 1 != len(target):
                return 0
            
            index = 0
            n = len(source)
            for i in range(len(target)):
                if index < n and target[i] == source[index]:
                    index += 1
            return index == n

        dp = [1]*m
        for i in range(1, m):
            count = 1
            for j in range(i-1,-1,-1):
                if len(words[j]) + 1 < len(words[i]):
                    break
                if calculate(words[j],words[i]):
                    count = max(count,dp[j]+1)
            dp[i] = count
        ##print(dp)
        return max(dp)