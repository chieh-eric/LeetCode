class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        max_candies = 0
        
        queue = deque()
        seen = set()
        visited = set()

        for box in initialBoxes:
            if status[box]:
                queue.append(box)
                visited.add(box)
            seen.add(box)
        
        while queue:
            i = queue.popleft()
            max_candies += candies[i]

            for key in keys[i]:
                status[key] = 1

            for box in containedBoxes[i]:
                seen.add(box)

            for box in seen:
                if status[box] and box not in visited:
                    queue.append(box)
                    visited.add(box)
        return max_candies
