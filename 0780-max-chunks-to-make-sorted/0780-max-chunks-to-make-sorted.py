class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        chunk = 0
        i = 0
        largest_index = -1
        while i < n:
            largest_index = max(largest_index,arr[i])
            if i == largest_index:
                chunk += 1
                i += 1  
                continue
            
            while i < largest_index:
                i += 1
                largest_index = max(largest_index,arr[i])
        return chunk

                      

    