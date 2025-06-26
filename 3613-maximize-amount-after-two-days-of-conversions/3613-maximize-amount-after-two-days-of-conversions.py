from collections import defaultdict
class Solution(object):
    def maxAmount(self, initialCurrency, pairs1, rates1, pairs2, rates2):
        """
        :type initialCurrency: str
        :type pairs1: List[List[str]]
        :type rates1: List[float]
        :type pairs2: List[List[str]]
        :type rates2: List[float]
        :rtype: float
        """
        day1_graph = defaultdict(list)
        day2_graph = defaultdict(list)
        intermediate = defaultdict(float)
        visited =  defaultdict(float)
        
        for i, (start, end) in enumerate(pairs1):
            day1_graph[start].append((end,rates1[i]))
            day1_graph[end].append((start,1/rates1[i]))
        
        for i, (start, end) in enumerate(pairs2):
            day2_graph[start].append((end,rates2[i]))
            day2_graph[end].append((start,1/rates2[i]))
            

        queue = deque()
        queue.append((initialCurrency,1.0))
        res = 0
        while queue:
            currency, rate = queue.popleft()
            for neighbor, amt in day1_graph[currency]:
                new_amt = rate*amt
                if new_amt > intermediate[neighbor]:
                    intermediate[neighbor] = new_amt
                    queue.append((neighbor,new_amt))

        for currency, rate in intermediate.items():
            queue.append((currency,rate))
            while queue:
                cur, amt = queue.popleft()
                if cur == initialCurrency:
                    res = max(res,amt)
                for neighbor, val in day2_graph[cur]:
                    new_amt = amt*val
                    if new_amt > visited[neighbor]:
                        visited[neighbor] = new_amt
                        queue.append((neighbor,new_amt))

        return res

