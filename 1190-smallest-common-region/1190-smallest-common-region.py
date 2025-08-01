class Node():
    def __init__(self,r):
        self.children = []
        self.name = str(r)
class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        dic = {}
        p= set()
        c = set()
        for r in regions:
            parent = r[0]
            p.add(parent)
            m = len(r)
            if parent not in dic:
                dic[parent] = Node(parent)
            for i in range(1,m):
                c.add(r[i])
                if r[i] not in dic:
                    dic[r[i]] = Node(r[i])
                dic[parent].children.append(dic[r[i]])

        root = (p-c).pop()
       # print(root)
        def find(node):
             
            found = []
            if node in dic:
                for child in dic[node].children:
                    res = find(child.name)
                    if res:
                        found.append(res)

            if node == region1 or node == region2 or len(found) >= 2:
                return node
            
            return found[0] if found else None
            #       0
            #      1     2 
            #    3,  4   9
            #  5 6  7,8
        return find(root)