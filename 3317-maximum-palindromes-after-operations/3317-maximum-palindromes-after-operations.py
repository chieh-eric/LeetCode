from collections import defaultdict
import heapq
class Solution(object):
    def maxPalindromesAfterOperations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic = defaultdict(int)
        length = []
        for word in words:
            length.append(len(word))
            for ch in word:
                dic[ch] += 1
        length.sort()
        valid = 0
        total_pairs = sum(v//2 for v in dic.values())
        total_center = sum(v%2 for v in dic.values())
        for l in length:
            need_pair = l // 2
            need_center = l % 2
          
            if need_pair <= total_pairs and need_center <= total_center:
                total_pairs -= need_pair
                total_center -= need_center
                valid += 1
            
            else:
                
                if need_pair + need_center <= total_pairs and need_center == 1:
                    total_pairs = total_pairs - need_pair - need_center
                    total_pairs += 1
                    valid += 1
                else:
                    break
        return valid

            
        