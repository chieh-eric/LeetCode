class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Approach
        # prfix sum of nums
        # [2,3,7,10,15]
        # Use dic -> key: length, val: must smaller than this value
        # dic[1] = 10, dic[2] = 5, dic[3] = 4, dic[4] = 3
        # iterate num, [0,2,3,7]
        # count = 4
        prefix = []
        prefix.append(0)
        count = 0
        less_than = {}
        n = len(nums)
        for i in range(1, n+1):
            less_than[i] = (k + i - 1) // i
        #print(less_than)


        def search(arr, index):
            m = len(arr)
            left = 0 
            right = m - 1
            
            def valid(i, j):
                if i == j:
                    return True
                #print(i,j)
                return (arr[i] - arr[j]) < less_than[i-j]
            while left < right:
                mid = (left + right) // 2
                if not valid(index, mid):
                    left = mid + 1
                else:
                    right = mid
            return left



        cur = 0
        for i, num in enumerate(nums):
            cur += num
            prefix.append(cur)
            idx = search(prefix, i+1)
            count += (i-idx+1)
        return count



