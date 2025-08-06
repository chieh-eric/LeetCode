class Solution(object):
    def amountPainted(self, paint):
        """
        :type paint: List[List[int]]
        :rtype: List[int]
        """
        parent = {}
        
        def find(x):
            if x not in parent:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        res = []
        for start, end in paint:
            painted = 0
            i = find(start)
            while i < end:
                painted += 1
                parent[i] = i + 1
                i = find(i+1)
            res.append(painted)
        return res
            
