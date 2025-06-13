class Solution(object):
    def minimumSemesters(self, n, relations):
        """
        :type n: int
        :type relations: List[List[int]]
        :rtype: int
        """
        graph = {}
        indegree = [0]*(n+1)
        indegree[0] = -1

        for preq, nxt in relations:
            if preq not in graph:
                graph[preq] = []
            graph[preq].append(nxt)
            indegree[nxt] += 1
        
        queue = deque()
        for i,value in enumerate(indegree):
            if value == 0:
                queue.append(i)
        
        taken_course = 0
        semester = 0
        while queue:
            semester += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                print(course)
                taken_course += 1
                if course in graph:
                    for neighbor in graph[course]:
                        
                        indegree[neighbor] -= 1
                        if indegree[neighbor] == 0:
                            queue.append(neighbor)
                
        return semester if taken_course == n else -1