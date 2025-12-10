class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # If substring has leading 0 and length > 1  -> break
        ans = []
        def dfs(index, path, value, last_mul):
            if index == len(num):
                if value == target:
                    ans.append(path)
                return
            
            for end in range(index+1, len(num) + 1):
                sub = num[index:end]
                curr = int(sub)

                if len(sub) > 1 and sub[0] == '0':
                    break
                
                if index == 0:
                    dfs(end, sub, curr, curr)
                else:
                    # +
                    dfs(end, path + "+" + sub, value + curr,curr)
                    dfs(end, path + "-" + sub, value - curr,-curr)
                    dfs(end, path + "*" + sub, value - last_mul + last_mul*curr, last_mul*curr)
        dfs(0,"",0,0)
        return ans
                    