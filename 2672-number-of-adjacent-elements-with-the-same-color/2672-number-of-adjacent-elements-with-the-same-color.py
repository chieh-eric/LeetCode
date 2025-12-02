class Solution(object):
    def colorTheArray(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        add = 0
        ans = []
        colors = [0]*n
        for index, color in queries:
            prev = colors[index]
            if color == prev:
                ans.append(add)
                continue
            if index > 0:
                if colors[index-1] != 0:
                    if colors[index-1] == prev:
                        add -= 1
                    elif colors[index-1] == color:
                        add += 1

            if index < n - 1:
                if colors[index+1] != 0:
                    if colors[index+1] == prev:
                        add -= 1
                    elif colors[index+1] == color:
                        add += 1
            colors[index] = color
            ans.append(add)
        return ans

