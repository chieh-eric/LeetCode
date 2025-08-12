class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def build(left,right, path):
            if left == n and right == n:
                res.append(path)
                return
            
            if left < n:
                build(left+1, right, path+"(")
            
            if right < left:
                build(left,right+1, path+")")
        

        build(0,0,"")
        return res