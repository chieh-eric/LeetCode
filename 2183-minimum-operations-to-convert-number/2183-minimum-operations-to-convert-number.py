class Solution(object):
    def minimumOperations(self, nums, start, goal):
        """
        :type nums: List[int]
        :type start: int
        :type goal: int
        :rtype: int
        """
        queue = deque()
        queue.append((start,0))
        n = len(nums)
        visited = set()
        while queue:
            val, op = queue.popleft()
            if val == goal:
                return op
            if 0 <= val <= 1000:
                for i in range(n):
                    add_val = val + nums[i]
                    if add_val not in visited:
                        queue.append((add_val,op+1))
                        visited.add(add_val)
                    minus_val = val - nums[i]
                    if  minus_val not in visited:
                        queue.append((minus_val,op+1))
                        visited.add(minus_val)
                    xor_val = val^nums[i]
                    if xor_val not in visited:
                        queue.append((xor_val,op+1))
                        visited.add(xor_val)
        return -1

