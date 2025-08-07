import random
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, words, master):
        """
        :type words: List[Str]
        :type master: Master
        :rtype: None
        """
        def match(w1,w2):
            return sum(w1[i] == w2[i] for i in range(6))

        for _ in range(30):
            
            guess_word = random.choice(words)
            #print(count)
            #print(count[guess_word])
            val = master.guess(guess_word)
            if val == 6:
                return
            words = [w for w in words if match(w,guess_word) == val]