from collections import defaultdict
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 4 :
            return []
        
        nums.sort()
        valid = set()
        for i in range(n):
            for j in range(i+1,n):
                aim = target - nums[i] - nums[j]
                left = j + 1
                right = n - 1
                while left < right:
                    if  nums[left] + nums[right] == aim:
                        valid.add(tuple([nums[i], nums[j], nums[left], nums[right]]))
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] > aim:
                        right -= 1
                    else:
                        left += 1
        #print(valid)
        return list(valid)

        