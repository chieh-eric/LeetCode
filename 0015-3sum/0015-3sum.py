class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            target = (-1)*nums[i]
            while(l<r):
                if target == nums[l] + nums[r]:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while(nums[l] == nums[l-1]) and l < r:
                        l+=1
                    r-=1
                    while(nums[r] == nums[r+1]) and l < r:
                        r-=1
                    
                if nums[l] + nums[r] > target:
                    r -=1
                elif nums[l] + nums[r] < target:
                    l +=1
        return res
