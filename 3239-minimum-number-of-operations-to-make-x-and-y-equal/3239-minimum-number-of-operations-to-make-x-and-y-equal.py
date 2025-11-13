class Solution(object):
    def minimumOperationsToMakeEqual(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Use BFS -> TC(for each x -> 4)
        queue = deque()
        queue.append((x,0))
        memo = {}
        while queue:
            num, op = queue.popleft()
            if num == y:
                return op
            memo[num] = op
            if num % 11 == 0 and num//11 not in memo:
                queue.append((num//11,op+1))
            
            if num % 5 == 0 and num // 5 not in memo:
                queue.append((num//5,op+1))
            
            if num + 1 not in memo:
                queue.append((num+1,op+1))
            if num > y and num - 1 not in memo:
                queue.append((num-1,op+1))
        


        