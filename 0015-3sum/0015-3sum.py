class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        result = {}
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            for j in range(i+1,len(nums),1):
                if target - nums[j] in result:
                    ans.add((nums[j],0-nums[i]-nums[j],nums[i]))
                result[nums[j]] = j
            result.clear()
        return [list(triplet) for triplet in ans]
