import heapq
class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        # Use BFS
        queue = []
        cur_lane = 2
        side_jumps = 0
        heapq.heappush(queue,(0, cur_lane, 0))

        n = len(obstacles)
        visited = set()

        while queue:
            step, state, point = heapq.heappop(queue)
            if (state, point) in visited:
                continue
            
            if point == n - 1:
                return step
            
            next_pos = point + 1
            visited.add((state,point))

            if next_pos < n and obstacles[next_pos] != state:
                heapq.heappush(queue, (step, state,next_pos))
                
            else:
                # Need side jump
                for i in range(1,4):
                    if obstacles[point] != i and i != state:
                        heapq.heappush(queue, (step+1, i, point))
            




