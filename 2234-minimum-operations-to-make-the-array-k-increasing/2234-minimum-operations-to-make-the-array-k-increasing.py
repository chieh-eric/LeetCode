import bisect
class Solution(object):
    def kIncreasing(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        res = [[] for _ in range(k)]
        lis = [[] for _ in range(k)]
        n = len(arr)
        for i in range(n):
            res[i%k].append(arr[i])

        op = 0
        for i, sub in enumerate(res):
            for num in sub:
                idx = bisect.bisect_right(lis[i],num)
                if idx == len(lis[i]):
                    lis[i].append(num)
                else:
                    lis[i][idx] = num
            op += len(sub) - len(lis[i])
        return op
