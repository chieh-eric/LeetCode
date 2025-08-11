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
        graph1 = defaultdict(list)
        for index, (i, j) in enumerate(pairs1):
            graph1[i].append((j,rates1[index]))
            graph1[j].append((i,1/float(rates1[index])))
        queue1 = deque()
        queue1.append((initialCurrency,1))
        day1 = defaultdict(float)

        while queue1:
            nxt, cur = queue1.popleft()
            for nei, rate in graph1[nxt]:
                if cur*rate > day1[nei]:
                    queue1.append((nei, cur*rate))
                    day1[nei] = (cur*rate)
        #print(day1)



        graph2 = defaultdict(list)
        for index, (i, j) in enumerate(pairs2):
            graph2[i].append((j,rates2[index]))
            graph2[j].append((i,1/float(rates2[index])))

        day2 = defaultdict(float)
        queue2 = deque()
        res = 1
        for start, init in day1.items():
            queue2.append((start,init))

            while queue2:
                nxt, cur = queue2.popleft()
                if nxt == initialCurrency:
                    res = max(res, cur)
                for nei, rate in graph2[nxt]:
                    if cur*rate > day2[nei]:
                        queue2.append((nei, cur*rate))
                        day2[nei] = (cur*rate)
        #print(day2)

        return res