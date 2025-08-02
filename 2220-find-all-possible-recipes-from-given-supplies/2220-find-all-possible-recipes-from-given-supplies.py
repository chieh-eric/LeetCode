from collections import defaultdict
class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        indegree = defaultdict(int)
        n = len(recipes)

        for i in range(n):
            for ingred in ingredients[i]:
                graph[ingred].append(recipes[i])
                indegree[recipes[i]] += 1

        queue = deque()
        for sup in supplies:
            queue.append(sup)
        
        res = []
        while queue:
            ingred = queue.popleft()
            for rec in graph[ingred]:
                indegree[rec] -= 1
                if indegree[rec] == 0:
                    queue.append(rec)
                    res.append(rec)
            
        #print(graph)
        return res