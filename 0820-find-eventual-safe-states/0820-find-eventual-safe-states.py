class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        states = [0]*n # 0 -> unvisited, 1 -> visiting, 2-> Safe
        def trace(node,states):
            if not graph[node] or states[node] == 2:
                return True

            if states[node] == 1:
                return False
            
            states[node] = 1
            for nei in graph[node]:
                if not trace(nei,states):
                    return False
            states[node] = 2
            return True

        res = []
        for i in range(n):
            if trace(i,states):
                res.append(i)
        return res