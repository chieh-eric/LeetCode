class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends == 1:
            return word
        n = len(word)
        max_length = n - (numFriends - 1)
        max_str = ""
        for i in range(n):
            candidate = word[i:]
            if len(candidate) > max_length:
                candidate = candidate[:max_length]
            if candidate > max_str:
                max_str = candidate
            
        return max_str 