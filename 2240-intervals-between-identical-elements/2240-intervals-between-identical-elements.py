from collections import defaultdict
class Solution(object):
    def getDistances(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # 0, 2, 3
        # 0, 2, 5
        dic = defaultdict(list)
        for i, num in enumerate(arr):
            dic[num].append(i)
        #print(dic)
        n = len(arr)
        res = [0]*n

        for key, ar in dic.items():
            l = len(ar)
            prefix = []
            cur = 0
            for val in ar:
                cur += val
                prefix.append(cur)
            #print(prefix)
            for i, index in enumerate(ar):
                left = ar[i] * i - prefix[i-1] if i > 0 else 0
                right = (prefix[l-1] - prefix[i]) - (l-i-1)*ar[i] if i < l - 1 else 0
                res[index] = left+right

        return res
