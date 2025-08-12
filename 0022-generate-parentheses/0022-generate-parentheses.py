class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def build(option, path):
            if not option:
                res.append("".join(path))
                return
            
            
            for key in option:
                copy = option.copy()
                copy[key] -= 1
                if copy[key] == 0:
                    del copy[key]

                if key == "(":
                    copy[")"] += 1
                path.append(key)
                build(copy,path)
                path.pop()


        count = Counter()
        count["("] = n
        build(count,[])
        #print(res)
        return res