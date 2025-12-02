from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(lambda: SortedList())
        for s, e in tickets:
            graph[s].add(e)
        
        # Dfs -> return the list of the smallest itinerary
        #print(graph)
        routes = []
        def dfs(pos):
            while graph[pos]:
                nxt_pos = graph[pos].pop(0)
                dfs(nxt_pos)
            routes.append(pos)

        dfs("JFK")
        #print(routes)
        return routes[::-1]