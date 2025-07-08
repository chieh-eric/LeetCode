import bisect
class Solution(object):
    def minOperations(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans = []
        n = len(nums)
        prefix = [0]*n
        cur = 0
        for i in range(n):
            cur += nums[i]
            prefix[i] = cur

        #print(prefix)
        for q in queries:
            
            idx = bisect.bisect_right(nums,q)
            #print(idx)
            if idx == 0:
                ans.append(prefix[n-1]-q*n)
            elif idx == n:
                ans.append(q*n - prefix[n-1])
            else:
                op = idx*q - prefix[idx-1]  
                op +=  (prefix[n-1] - prefix[idx-1]) - (n-idx)*q
                ans.append(op)
        return ans