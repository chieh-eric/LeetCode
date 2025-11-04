from collections import defaultdict
class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)

        ans = []
        dic = defaultdict(int)
        left = 0

        for i in range(n):
            
            dic[nums[i]] += 1
            while i - left + 1 > k:
                dic[nums[left]] -= 1
                left += 1
            if i - left + 1 == k:
                temp = []
                for key, val in dic.items():
                    temp.append((val,key))
                temp.sort(key=lambda x:(-x[0],-x[1]))
                total = 0
                for j in range(min(x, len(temp))):
                    total += temp[j][1]*temp[j][0]
                ans.append(total)
        return ans