from collections import defaultdict
class Solution(object):
    def numberOfSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def calculate(count):
         
            return count*(count+1)//2
        
        res = 0
        dic = defaultdict(int)
        stack = []
        for num in nums:
            while stack and num > stack[-1]:
                res += calculate(dic[stack[-1]])
                dic[stack[-1]] = 0
                stack.pop()
            stack.append(num)
            dic[num] += 1
        for key in dic:
            res += calculate(dic[key])
        return res