from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubsequence(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dic = defaultdict(int)
        dic[0] = 0
        for num in nums:
            temp = dic.copy()
            for key in temp:
                if key + num > target:
                    continue
                dic[key+num] = max(dic[key+num],temp[key] + 1)
           # print(dic)
        return dic[target] if dic[target] != 0 else -1