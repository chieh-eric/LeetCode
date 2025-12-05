class Solution(object):
    def pourWater(self, heights, volume, k):
        """
        :type heights: List[int]
        :type volume: int
        :type k: int
        :rtype: List[int]
        """
        n = len(heights)
        def find(direction):
            cur = k
            best = k
            while n > cur + direction >= 0 and heights[cur+direction] <= heights[cur]:
                if heights[cur+ direction] < heights[best]:
                    best = cur + direction
                cur += direction
            return best

        n = len(heights)
        for _ in range(volume):
            idx = find(-1)
            if idx != k:
                heights[idx] += 1
                continue
            idx = find(1)
            heights[idx] += 1
        return heights

