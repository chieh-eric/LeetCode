from collections import defaultdict
class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        original = [(num,i) for i, num in enumerate(nums)]
        original.sort()
        groups = defaultdict(list)
        groups[0].append(original[0])
        key = 0
        n = len(nums)
        for i in range(1,n):
            if original[i][0] - original[i-1][0] > limit:
                key += 1
            groups[key].append(original[i])
        res = [0]*n
        #print(groups)

        for key in groups:
            group = groups[key]
            idxs = sorted([idx for _,idx in group])
            for i, idx in enumerate(idxs):
                res[idx] = group[i][0]
        return res
