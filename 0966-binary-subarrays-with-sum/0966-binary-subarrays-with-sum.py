class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefix = Counter()
        prefix[0] = 1
        cur = 0
        count = 0
        for i, num in enumerate(nums):
            cur += num
            target = cur - goal
            
            if target in prefix:
                count += prefix[target]
            prefix[cur] += 1
            #print(count)
            
        #print(count)
        return count