class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = []
        i = j = 0
        n = len(word1)
        m = len(word2)

        while i < n and j < m:
            if word1[i:] > word2[j:]:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1

        while word1[i:]:
            res.append(word1[i])
            i += 1

        while word2[j:]:
            res.append(word2[j])
            j += 1

        return "".join(res)