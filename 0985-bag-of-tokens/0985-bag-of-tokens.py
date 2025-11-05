class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        max_score = 0
        n = len(tokens)
        l, r = 0, n - 1
        tokens.sort()
        max_score = 0
        cur_score = 0
        cur_power = power
        while l <= r:
            while l <= r and cur_power >= tokens[l]:
               cur_score += 1
               cur_power -= tokens[l]
               l += 1
            max_score = max(max_score, cur_score)
            if l <= r and cur_score > 0:
                cur_score -= 1
                cur_power += tokens[r]
                r -= 1
            else:
                break
        return max_score
        