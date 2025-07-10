import bisect
class Solution(object):
    def kIncreasing(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
       
        op = 0
        n = len(arr)
        for j in range(k):
            sub = []
            for i in range(j,n,k):
                num = arr[i]
                idx = bisect.bisect_right(sub,num)
                if idx == len(sub):
                    sub.append(num)
                else:
                    sub[idx] = num
            op += len(sub)
        return n - op
