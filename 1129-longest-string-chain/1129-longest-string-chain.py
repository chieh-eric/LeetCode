class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        m = len(words)
        words.sort(key=lambda x:len(x))
        dic = {}
        for word in words:
            dic[word] = 1
            for i in range(len(word)):
                cut_word = word[:i] + word[i+1:]
                if cut_word in dic:
                    dic[word] = max(dic[word], dic[cut_word] + 1)
        return max(dic.values())