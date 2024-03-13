class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*len(s)
        for i in range(len(s)):
            for word in wordDict:
                if len(word)-1 > i:
                    continue
                if dp[i-len(word)] or i ==len(word)-1 :
                    if s[i-len(word)+1:i+1] == word :
                        dp[i] = True
                        break
        return dp[-1]