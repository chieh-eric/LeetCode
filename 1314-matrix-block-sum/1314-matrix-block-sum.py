class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        #[1,2,3],
        #[4,5,6],
        #[7,8,9]]

        n = len(mat)
        m = len(mat[0])
        prefix_row = [[0]* m for _ in range(n)]
        ans = [[0]* m for _ in range(n)]
        # TC(M*N*K)

        for i in range(n):
            cur = 0
            for j in range(m):
                cur += mat[i][j]
                prefix_row[i][j] = cur
        #print(prefix_row)

        for i in range(n):
            for j in range(m):
                total = 0
                min_index = max(0, j - k)
                max_index = min(m-1, j + k)
                #print(min_index, max_index)
                for ik in range(max(0,i-k), min(n,i+k+1)):
                    #print(ik)
                    #print(prefix_row[ik][max_index], prefix_row[ik][min_index],  mat[ik][min_index])
                    total += (prefix_row[ik][max_index] - prefix_row[ik][min_index] + mat[ik][min_index])
                ans[i][j] = total
        return ans
                    


        