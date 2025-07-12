class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        left = [0]*n
        right = [0]*n
        stack = []
        op = 0
        mod = 10**9 + 7

        for i in range(n):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i],count))
            left[i] = count
        #print(left)

        stack = []
        for i in range(n-1,-1,-1):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i],count))
            right[i] = count
        #print(right)

        for i in range(n):
            op += arr[i]*left[i]*right[i]
        return op % mod