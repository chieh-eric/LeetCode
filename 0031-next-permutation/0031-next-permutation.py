class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 1 5 4 3 2
        def reverse(i,j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        index = -1
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                index = i - 1
                break
        #print(index)
        if index == -1:
            reverse(0,n-1)
        else:
            for j in range(n-1,index, -1):
                if nums[j] > nums[index]:
                    #print("hi")
                    nums[j], nums[index] = nums[index], nums[j]
                    break
            reverse(index+1,n-1)