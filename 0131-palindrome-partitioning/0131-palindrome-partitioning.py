class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        n = len(s)
        is_palindrome = [[False]*n for _ in range(n)]

        for length in range(1,n+1):
            for i in range(n-length+1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length <= 2:
                        is_palindrome[i][j] = True
                    else:
                        is_palindrome[i][j] = is_palindrome[i+1][j-1]
        #print(is_palindrome)
        def backtrack(i,path):
            if i == n :
                r = []
                start = 0
                print(path)
                for p in path:
                    r.append(s[start:p])
                    start = p
                res.append(r)
                return
            
            for j in range(i,n):
                if is_palindrome[i][j]:
                    
                    path.append(j+1)
                  
                    backtrack(j+1,path)
                    path.pop()
        backtrack(0,[])
        #print(res)
        return res