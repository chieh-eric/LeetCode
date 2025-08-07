from collections import defaultdict
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic = defaultdict(int)
        words.sort(key = lambda x:len(x))
        for word in words:
            for i in range(len(word)):
                dic[word] = max(dic[word],dic[word[:i]+word[i+1:]]+1)
        return max(dic.values()) 