class Solution(object):
    def wordCount(self, startWords, targetWords):
        """
        :type startWords: List[str]
        :type targetWords: List[str]
        :rtype: int
        """
        availabe = {}
        for word in startWords:
            availabe[tuple(sorted(word))] = True
        #print(availabe)

        count = 0
        for word in targetWords:
            n = len(word)
            cur = ""
            for i in range(n):
                cur = word[:i] + word[i+1:]
                if tuple(sorted(cur)) in availabe:
                    count += 1
                    break
        return count