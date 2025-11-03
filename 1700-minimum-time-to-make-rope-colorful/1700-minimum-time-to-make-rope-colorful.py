class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        n = len(colors)
        i = 0

        ans = 0
        while i < n:
            color = colors[i]
            max_time = total_time = 0
            total_time = 0
            while i < n and color == colors[i]:
                max_time = max(max_time, neededTime[i])
                total_time += neededTime[i]
                i += 1
            ans += (total_time - max_time)
        return ans

        