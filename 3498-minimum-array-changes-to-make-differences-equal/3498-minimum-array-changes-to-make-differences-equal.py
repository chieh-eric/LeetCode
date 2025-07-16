from collections import defaultdict
import bisect
class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = defaultdict(int)
        n = len(nums)
        half = n //2
        left = 0
        right = n - 1
        max_tolerent = [0]* half
        while right > left:
            dic[abs(nums[right]-nums[left])] += 1
            max_tolerent[left] = max(k-min(nums[right],nums[left]),max(nums[right],nums[left]))
            left += 1
            right -= 1
        max_tolerent.sort()
        #print(max_tolerent)
        #print(dic)
        min_op = float('inf')
        # [ 16, 17, 19 ,19, 19, 19, 19, 20, 20, 20]
        for key in dic:
            idx = bisect.bisect_left(max_tolerent,key)
            #print(key)
            #print(idx)
            op = (half-idx) - dic[key]
            op += idx*2
            min_op = min(min_op,op)
        return min_op