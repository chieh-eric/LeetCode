from collections import defaultdict
class Solution(object):
    def minimumOperationsToWriteY(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # For not Y, make the majoirty freq become to all, make Y majority to all but can't equal to not Y
        # Make majority freq of Y become to all, and make not Y majoiry to all but can't equal to Y

        y_dic = {0:0, 1:0, 2:0}
        y_count = 0
        noty_dic = {0:0, 1:0, 2:0}
        other_count = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if (i == j and i <= n // 2) or ((i+j) == n - 1 and i <= n//2) or (j == n // 2 and i >= n // 2):
                    y_dic[grid[i][j]] += 1
                    y_count += 1    
                else:
                    noty_dic[grid[i][j]] += 1
                    other_count += 1
   
        not_y = []
        y = []
        for key, count in noty_dic.items():
            not_y.append((key,count))
        
        for key, count in y_dic.items():
            y.append((key,count))
        
        not_y.sort(key=lambda x:-x[1])
        y.sort(key=lambda x:-x[1])
        
        res = 0
        if not_y[0][0] != y[0][0]:
            res += (y_count - y[0][1]) + (other_count - not_y[0][1])
        else:
            # Let y use major
            y_diff = y_count - y[0][1] + not_y[0][1] +  not_y[2][1]

            # Other
            other_diff = other_count - not_y[0][1] + y[0][1] + y[2][1]
            res = min(other_diff, y_diff)
        return res


            

        


