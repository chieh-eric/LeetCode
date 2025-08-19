class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        inf = float('inf')
        stack = []
        res = 0
        nums1 = [inf] + nums + [inf]

        for i, num in enumerate(nums1):

            while stack and nums1[stack[-1]] < nums1[i]:
                j = stack.pop()
                k = stack[-1]
                res += nums1[j]*(i-j)*(j-k)
            
            stack.append(i)
        
        stack = []
        nums1 = [-inf] + nums + [-inf]
        for i, num in enumerate(nums1):

            while stack and nums1[stack[-1]] > nums1[i]:
                j = stack.pop()
                k = stack[-1]
                res -= nums1[j]*(i-j)*(j-k)
            stack.append(i)
        return res