class UnionFind():
    def __init__(self,n):
        self.parent = [v for v in range(n)]
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[px] = py

class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
    
        n = len(strs)
        u = UnionFind(n)
        
        for i in range(1,n):
            word = strs[i]
            #print(word)
            for j in range(i):
                target = strs[j]
                #print(target)
                valid = False
                difference = 0
                word_want = target_want = ""
                for k in range(len(word)):
                    if word[k] != target[k]:
                        #print("hi")
                        difference += 1
                        if difference == 1:
                            word_want = target[k]
                            target_want = word[k]
                        elif difference == 2:
                            if word[k] == word_want and target[k] == target_want:
                                #print("hgudad")
                                valid = True
                if (valid and difference == 2) or word == target:
                    u.union(i,j)
        group = set()
        for i in range(n):
            pi = u.find(i)
            group.add(pi)
            #print(i,pi)
        #print(group)
        return len(group)

        # kccomwcgcs
        # socgcmcwkc
        # sgckwcmcoc
        # coswcmcgkc
        # cowkccmsgc
        # cosgmccwkc