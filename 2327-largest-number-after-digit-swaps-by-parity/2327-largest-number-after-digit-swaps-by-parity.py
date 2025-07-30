class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        even = []
        odd = []
        n  = len(str(num))
        for i, nu in enumerate(str(num)):
            if int(nu) % 2:
                odd.append((int(nu),i))
            else:
                even.append((int(nu),i))
        even_index = sorted([v[1] for v in even])
        odd_index = sorted([v[1] for v in odd])

        even.sort(reverse =True)
        odd.sort(reverse =True)
        #print(even_index)
        res = [0]*n
        for i in range(len(even)):
            res[even_index[i]] = str(even[i][0])
        for i in range(len(odd)):
            res[odd_index[i]] = str(odd[i][0])
        #print(res)
        return int("".join(res))

        
        
