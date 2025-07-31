import random
import bisect
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.arr = []
        total = sum(w)
        cur = 0
        for i, wei in enumerate(w):
            cur += (float(wei)/total)
            self.arr.append(cur)

    def pickIndex(self):
        """
        :rtype: int
        """
        val = random.random()
        idx = bisect.bisect_left(self.arr,val)
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()