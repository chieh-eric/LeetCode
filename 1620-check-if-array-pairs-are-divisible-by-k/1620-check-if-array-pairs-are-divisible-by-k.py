from collections import defaultdict
class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        # Approach
        # Use dictionary, -> key element value % k
        # Every iteration, look up (k - current element)
        # (2,3), (1,4), (5, 10), (7,8), (1,9)
        dic = defaultdict(int)
        for val in arr:
            find = (k - val) % k
            mod_val = val % k 
            if dic and find in dic:
                dic[find] -= 1
                if dic[find] == 0:
                    del dic[find]
            else:
                dic[mod_val] += 1

        return True if not dic else False




        