from collections import defaultdict
class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        dic = defaultdict(int)
        for num in nums:
            dic[num%value] += 1
        
        #print(dic)
        min_val = max(dic, key = dic.get)
        #print(min_val)
        if len(dic) != value:
            for i in range(value):
                if i not in dic:
                    return i
        else:
            min_val = min(dic.items(), key = lambda x:(x[1],x[0]))[0]
            #print("hi")
            return dic[min_val]*value + min_val
        