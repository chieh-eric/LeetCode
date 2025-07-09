from collections import defaultdict
class Solution(object):
    def maximumSetSize(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        threshold = n //2
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        valid = set()
        for num in nums1:
            dic1[num] += 1
        for num in nums2:
            dic2[num] += 1
        
        

        item1 = item2 = 0
        for key in dic1:
            if key not in dic2 and item1 < threshold:
                valid.add(key)
                item1 += 1
        
        for key in dic2:
            if key not in dic1 and item2 < threshold:
                valid.add(key)
                item2 += 1
        #print(valid)
        for key in dic1:
            #print(item1)
            if key in dic2 and item1 < threshold:
                valid.add(key)
                item1 += 1
        
        for key in dic2:
            #print(item2)
            if key in dic1 and item2 < threshold and key not in valid:
                valid.add(key)
                item2 += 1
        #print(valid)      
        return len(valid)
        
