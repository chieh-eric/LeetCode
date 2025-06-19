from collections import defaultdict
class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
       
        dic = defaultdict(list)
        n = len(word)
        for i in range(n):
            dic[ord(word[i])].append(i)
        count = 0
        for key in dic:
            if key+32 in dic and dic[key+32][-1] < dic[key][0]:
                count += 1
            
        return count