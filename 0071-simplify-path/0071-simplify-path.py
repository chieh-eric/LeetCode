class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ans = []
        n = len(path)
        i = 0
        while i < n and path[i] == "/":
            i += 1

        while i < n:
            temp = ""
            while i < n and path[i] != "/":
                temp += path[i]
                i += 1
            if temp == "..":
                if ans:
                    ans.pop()
            elif temp != ".":
                ans.append(temp)
            while i < n and path[i] == "/":
                i += 1
            
        return "/" + "/".join(ans)

        