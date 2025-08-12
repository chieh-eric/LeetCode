from itertools import permutations
class Solution(object):
    def minimumString(self, a, b, c):
        """
        :type a: str
        :type b: str
        :type c: str
        :rtype: str
        """
        def combine(x,y):
            if y in x:
                return x
            if x in y:
                return y
            
            overlap = 0
            for i in range(1,min(len(x),len(y))+1):
                if x[-i:] == y[:i]:
                    overlap = i

            return x + y[overlap:]
        min_len = float('inf')
        min_str = ""
        res = [a,b,c]
       
        for perm in permutations(res):
            l = combine(perm[0],combine(perm[1],perm[2]))
            #print(l)
            #print(r)
            if len(l) < min_len:
                min_len = len(l)
                min_str = l
            elif len(l) == min_len:
                #print(l)
                #print(min_str)
                min_str = min(min_str,l)
            

        return min_str