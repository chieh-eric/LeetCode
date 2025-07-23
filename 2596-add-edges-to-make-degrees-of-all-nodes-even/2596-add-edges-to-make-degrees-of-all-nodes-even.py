class Solution(object):
    def isPossible(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        all_node = set(range(1,n+1))
        dic = {}
        for i, j in edges:
            if i not in dic:
                dic[i] = set()
                dic[i].add(i)
            dic[i].add(j)

            if j not in dic:
                dic[j] = set()
                dic[j].add(j)
            dic[j].add(i)
        
        pair = set()
        for key in dic:
            if len(dic[key]) % 2 == 0:
                pair.add(key)
        #print(pair)
        if not pair:
            return True

        if len(pair) % 2 or len(pair) > 4:
            return False

        if len(pair) == 2:
            a, b = list(pair)
            #print(dic[b])
            if a not in dic[b]:
                return True
            not_connect = all_node - dic[a] - dic[b]
            if not_connect:
                return True
            return False

        if len(pair) == 4:
            a, b, c, d = list(pair)
            possibles = [[(a,b),(c,d)], [(a,c),(b,d)], [(a,d),(b,c)]]
            
            for (u1,v1), (u2,v2) in possibles:
                if v1 not in dic[u1] and v2 not in dic[u2]:
                    return True
            return False
        

            