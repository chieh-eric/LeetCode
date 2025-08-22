from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = wordList + [beginWord]
        n = len(wordList)
        ones = defaultdict(list)
        if endWord not in wordList:
            return 0

       
        used = set()

        queue = deque()
        queue.append((beginWord,1))
        wordSet = set(wordList)
        while queue:
            word, step = queue.popleft()
            if word in used:
                continue
            
            if word == endWord:
                return step

            used.add(word)
            for l in range(len(beginWord)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:l] + ch + word[l+1:]
                    if new_word in wordSet:
                        wordSet.remove(new_word)

                        queue.append((new_word, step + 1))
        return 0