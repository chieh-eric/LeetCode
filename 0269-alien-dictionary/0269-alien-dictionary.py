from collections import defaultdict
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = defaultdict(list)
        indegree = {ch:0 for word in words for ch in word}
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            
            for k in range(min(len(w1), len(w2))):
                if w1[k] != w2[k]:
                    graph[w1[k]].append(w2[k])
                    indegree[w2[k]] += 1
                    break

        queue = deque()
        for ch in indegree:
            if indegree[ch] == 0:
                queue.append(ch)
        
        result = []
        while queue:
            ch = queue.popleft()
            result.append(ch)

            for nei in graph[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        # cycle
        if len(result) != len(indegree):
            return ""
        return "".join(result)