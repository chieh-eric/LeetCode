class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        terminal = set()
        for i, nei in enumerate(graph):
            if len(nei) == 0:
                terminal.add(i)
        n = len(graph)
        states = [0]*n
        def trace(node,states):
            if not graph[node] or node in terminal:
                return True

            if states[node] == 1 and node not in terminal:
                return False
            
            states[node] = 1
            res = True
            for nei in graph[node]:
                res = res and trace(nei,states)
                if res:
                    terminal.add(nei)
            if res:
                terminal.add(node)
            return res

        for i in range(n):
            states = [0]*n
            if i not in terminal:
                trace(i,states)
        return sorted(list(terminal))