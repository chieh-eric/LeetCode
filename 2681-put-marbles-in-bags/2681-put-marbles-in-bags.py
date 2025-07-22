class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 0
        n = len(weights)
        wei = []
        for i in range(n-1):
            wei.append(weights[i]+weights[i+1])
        wei.sort()
        return sum(wei[-k+1:]) - sum(wei[:k-1])