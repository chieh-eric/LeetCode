class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # Get value of last position
        # Two condition
        # 7, 3
        last_element1 = nums1[-1]
        last_element2 = nums2[-1]
        
        # Condition1 -> last_element1 is in nums1
        n = len(nums1)
        count1 = 0
        c1_nums1 = nums1[::]
        c1_nums2 = nums2[::]
        for i in range(n-1):
            if last_element1 < c1_nums1[i]:
                if last_element1 < c1_nums2[i]:
                    count1 = float('inf')
                    break
                else:
                    c1_nums2[i] = c1_nums1[i]
                    count1 += 1
        for i in range(n-1):
            if last_element2 < c1_nums2[i]:
                if last_element2 < c1_nums1[i] or last_element1 < c1_nums2[i]:
                    count1 = float('inf')
                    break
                else:
                    count1 += 1
        

        # Condition2 -> last_element1 is in nums2
        c2_nums1 = nums1[::]
        c2_nums2 = nums2[::]
        count2 = 1
        for i in range(n-1):
            if last_element2 < c2_nums1[i]:
                if last_element2 < c2_nums2[i]:
                    return -1
                else:
                    c2_nums2[i] = c2_nums1[i]
                    count2 += 1
        for i in range(n-1):
            if last_element1 < c2_nums2[i]:
                if last_element1 < c2_nums1[i] or last_element2 < c2_nums2[i]:
                    return -1
                else:
                    count2 += 1
        #print(count1, count2)
        min_val = min(count1, count2)
        return  min_val 
