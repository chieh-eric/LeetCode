class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        arr = [0]*n
        cur = 0
        step = 0

        for i in range(n):
            cur += arr[i]
            #print(cur)
            if (nums[i] and cur % 2 == 0) or (nums[i] == 0 and cur % 2):
                #print(i)
                continue
            right = i + k - 1
            if right >= n:
                return -1

            cur += 1
            if right + 1 < n:
                arr[right+1] -= 1
            step += 1
        #print(arr)
        return step