from collections import defaultdict
import bisect
class Solution(object):
    def minWindow(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: str
        """
        # dic key -> alpha, value index
        dic = defaultdict(list)
        for i, val in enumerate(s1):
            dic[val].append(i)
        #print(dic)
        n = len(s1)
        m = len(s2)

        min_length = float('inf')
        ans_left = None
        ans_right = None


        if s2[0] not in dic:
            return ""
        

        for start in dic[s2[0]]:
            cur_index = start
            s2_index = 1
            found = True
            while s2_index < m:
                nxt_idx = bisect.bisect_right(dic[s2[s2_index]], cur_index)
                if nxt_idx == len(dic[s2[s2_index]]):
                    found = False
                    break
                cur_index = dic[s2[s2_index]][nxt_idx]
                s2_index += 1
            if found and cur_index - start + 1 < min_length:
                ans_left = start
                ans_right = cur_index + 1
                min_length = cur_index - start + 1
        return s1[ans_left:ans_right] if min_length != float('inf') else ""
            




        
        
        


