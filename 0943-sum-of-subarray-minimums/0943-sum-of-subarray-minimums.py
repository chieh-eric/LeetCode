class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        count = [1]*n
        stack = []
        op = 0
        mod = 10**9 + 7
        prev = 0
        for i in range(n):
            modify = False
            while stack and stack[-1][0] > arr[i]:
                count[i] += count[stack[-1][1]]
                stack.pop()
                modify = True
                
            stack.append((arr[i],i))
            if modify:
                total = 0
                for item in stack:
                    val, index = item
                    total += val*count[index]
                op += total
                prev = total
            else:
                op += prev + arr[i]
                prev = prev + arr[i]
        #print(count)
        return op % mod
