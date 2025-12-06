class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        stack = []
        for val in nums2:
            while stack and stack[-1] < val:
                dic[stack.pop()] = val
            stack.append(val)
        res = []
        for val in nums1:
            if val not in dic:
                res.append(-1)
            else:
                res.append(dic[val])
        return res