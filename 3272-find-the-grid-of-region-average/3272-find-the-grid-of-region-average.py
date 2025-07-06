class Solution(object):
    def resultGrid(self, image, threshold):
        """
        :type image: List[List[int]]
        :type threshold: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])

        def isValidRegion(i,j):
            for x in range(3):
                for y in range(3):
                    target_x = x + i
                    target_y = y + j
                    direction = [(0,1),(1,0),(0,-1),(-1,0)]
                    for dx, dy in direction:
                        nx = target_x + dx
                        ny = target_y + dy
                        if i <= nx < i+3 and j <= ny < j+3 and abs(image[nx][ny] - image[target_x][target_y]) > threshold:
                            return False
            return True

        contribution = [[0]*n for _ in range(m)]
        counts = [[0]*n for _ in range(m)]
        for i in range(m - 2):
            for j in range(n - 2):
                
                if isValidRegion(i,j):
                    total = 0
                    for a in range(3):
                        for b in range(3):
                            total += image[i+a][j+b]
                    
                    avg = total // 9

                    for a in range(3):
                        for b in range(3):
                            contribution[i+a][j+b] += avg
                            counts[i+a][j+b] += 1
        result = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if counts[i][j] > 0:
                    result[i][j] = contribution[i][j] // counts[i][j]
                else:
                    result[i][j] = image[i][j]
        return result

