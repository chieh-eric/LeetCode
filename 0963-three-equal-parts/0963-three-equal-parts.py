from collections import Counter
class Solution(object):
    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        count = Counter(arr)
        if count[1] % 3:
            return [-1,-1]
        
        if count[0] == n:
            return [0,n-1]


        one_pos = [i for i, bit in enumerate(arr) if bit == 1]
        target = count[1] // 3

        i1 = one_pos[0]
        i2 = one_pos[target]
        i3 = one_pos[target*2]

        while i3 < n:
            if arr[i1] != arr[i2] or arr[i2] != arr[i3]:
                return [-1,-1]
            i1 += 1
            i2 += 1
            i3 += 1
        
        return [i1-1,i2]


            