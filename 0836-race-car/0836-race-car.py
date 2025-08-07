class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        queue = deque()
        queue.append((0,1,0))

        while queue:
            pos, speed, step = queue.popleft()
            if pos == target:
                return step
            
            # Do A operation
            
            queue.append((pos+speed, speed*2, step + 1))
            
            if (target < pos + speed and speed > 0) or (target > pos + speed and speed < 0):
                queue.append((pos,-speed/abs(speed),step+1))
        
