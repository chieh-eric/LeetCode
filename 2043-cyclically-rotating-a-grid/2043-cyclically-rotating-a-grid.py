class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Approach
        # BruteForce, for each layer, two iteration
        # 1. collection element
        # 2. place the rorated element

        n = len(grid)
        m = len(grid[0])
        new_matrix = [[0]*m for _ in range(n)]
        top = 0
        right = m - 1
        bottom = n - 1
        left = 0

        while top <= bottom and left <= right:
            # 1. collect element
            elements = []
            pos = []
            # horizontal left -> right
            for j in range(left, right + 1):
                elements.append(grid[top][j])
                pos.append((top, j))
            top += 1
            # vertical top -> bottom
            for j in range(top, bottom + 1):
                #print(j,right)
                elements.append(grid[j][right])
                pos.append((j, right))
            right -= 1
            # horizontal right -> left
            if right >= left:
                for j in range(right, left - 1, -1):
                    elements.append(grid[bottom][j])
                    pos.append((bottom, j))
            bottom -= 1
            # vertical bottom -> top
            if right >= left:
                for j in range(bottom, top - 1, -1):
                    elements.append(grid[j][left])
                    pos.append((j, left))
            left += 1
            #print(elements)
            # 2. place in ratated order
            length = len(elements)
            
            index = 0
            while index < length:
                cur_index = (index + k) % length
                cur_i, cur_j = pos[index]
                new_matrix[cur_i][cur_j] = elements[cur_index]
                index += 1
        
        return new_matrix