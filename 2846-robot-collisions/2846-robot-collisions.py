class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        stack = []
        n = len(positions)
        res = [0]*n
        combine = sorted([(positions[i],healths[i],directions[i],i) for i in range(n)],key=lambda x:x[0])

        i = 0
        #print(combine)
        while i < n:
            pos = combine[i][0]
            heal = combine[i][1]
            d = combine[i][2]
            idx = combine[i][3]

            if d == "L":
              
                while stack and heal > stack[-1][0]:
                    heal -= 1
                    stack.pop()
                
                if not stack:
                    res[idx] = heal
                else:
                    if heal < stack[-1][0]:
                        stack[-1] = (stack[-1][0]-1, stack[-1][1])
                    else:
                        stack.pop()
            else:
               
                stack.append((heal,idx))
           
            i += 1
        while stack:
            res[stack[-1][1]] = stack[-1][0]
            stack.pop()
        ans = []
        for i in range(n):
            if res[i] != 0:
                ans.append(res[i])
        return ans