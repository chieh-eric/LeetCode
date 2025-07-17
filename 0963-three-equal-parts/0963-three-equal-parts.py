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


        count_one = count[1] // 3
        last_pointer  = -1
        slide = Counter()
        
        for i in range(n-1,-1,-1):
            slide[arr[i]] += 1
            if slide[1] == count_one:
                last_pointer = i
                break
        
        first_pointer = -1
        common = arr[last_pointer:]
        #print(common)
        m = len(common)
        for i in range(n):
            if  arr[i] == 1:
                first_pointer = i
                break
        first_split = first_pointer + m - 1

        #print(arr[first_pointer:first_split+1])
        if arr[first_pointer:first_split+1] != common:
            return [-1,-1]
        
        second_pointer = -1
        for i in range(first_split+1,n):
            if arr[i] == 1:
                second_pointer = i
                break
        second_split = second_pointer + m

        #print(second_pointer)
        #print(second_split)
        #print(arr[second_pointer:second_split])
        if arr[second_pointer:second_split] != common:
            return [-1,-1]
        
        return [first_split,second_split]


            