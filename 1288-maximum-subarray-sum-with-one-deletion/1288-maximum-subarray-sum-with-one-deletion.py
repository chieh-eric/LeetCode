class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        no_delete = [0]*n
        one_delete = [0]*n

        no_delete[0] = arr[0]
        one_delete[0] = -float('inf')

        for i in range(1,n):
            no_delete[i] = max(no_delete[i-1] + arr[i],arr[i])
            one_delete[i] = max(one_delete[i-1] + arr[i],no_delete[i-1])
       
        return max(max(one_delete),max(no_delete))