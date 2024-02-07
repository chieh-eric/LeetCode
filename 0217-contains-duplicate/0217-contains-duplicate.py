class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            else:
                dic[nums[i]] = i
        return False