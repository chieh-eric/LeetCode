class Solution(object):
    def colorTheArray(self, N, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(queries)
        pair = 0
        arr = [0]*N
        ans = []

        for idx, color in queries:
            var = 0
            if arr[idx] == color:
                ans.append(pair)
                continue

            if idx - 1 >= 0:
                if arr[idx-1] == color:
                    pair += 1
                
                if arr[idx-1] == arr[idx] and arr[idx] != 0:
                    pair -= 1
                
                
            if idx + 1 < N:
                if arr[idx+1] == color:
                    pair += 1
                
                if arr[idx+1] == arr[idx] and arr[idx] != 0:
                    pair -= 1

            arr[idx] = color
            ans.append(pair)
        return ans
