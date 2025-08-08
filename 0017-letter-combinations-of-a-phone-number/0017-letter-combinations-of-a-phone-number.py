class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        n = len(digits)
        letter = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def backtrack(i,path):
            if i == n:
                out = "".join(path[:])
                if out:
                    res.append(out)
                return
            
            for ch in letter[digits[i]]:
                path.append(ch)
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return res
            
