import heapq
class Solution(object):
    def findMaxSum(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums1_pair = []
        for i, num in enumerate(nums1):
            nums1_pair.append((num, i))
        nums1_pair.sort()
        
        n = len(nums1)
        ans = [0]*n

        same_list = []
        window = []
        prev_val = None
        cur_val = 0
        occupy = 0
        #print(nums1_pair)
        for val, index in nums1_pair:
            if prev_val and val > prev_val:
                for nums2_val in same_list:
                    if occupy >= k:
                        if window[0] < nums2_val:
                            p = heapq.heappop(window)
                            cur_val -= p
                            cur_val += nums2_val
                            heapq.heappush(window, (nums2_val))
                    else:
                        heapq.heappush(window, (nums2_val))
                        cur_val += nums2_val
                        occupy += 1
                same_list = [] 
            same_list.append(nums2[index])
            ans[index] = cur_val
            prev_val = val
        return ans