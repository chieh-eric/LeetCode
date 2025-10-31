from collections import defaultdict
class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        dic = defaultdict(list)
        max_val = 0
        for i, num_list in enumerate(nums):
            for j, num in enumerate(num_list):
                dic[(i+j)].append(num)
                max_val = max(max_val, i+j)
        ans = []
        for i in range(max_val+1):
            ans.extend(reversed(dic[i]))
        return ans
        
                

        