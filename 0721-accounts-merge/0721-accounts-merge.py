from collections import defaultdict
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        graph = defaultdict(list)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            prev = None
            for i in range(1, len(account)):
                email_to_name[account[i]] = name
                if prev:
                    graph[account[i]].append(prev)
                    graph[prev].append(account[i])
                prev = account[i]
        #print(graph)
        #print(email_to_name)
        visited = set()
        def dfs(email):
            path = [email]
            visited.add(email)
            for nei in graph[email]:
                if nei not in visited:
                    path.extend(dfs(nei))
            return path

        res = []
        for email, name in email_to_name.items():
            if email not in visited:
                path = sorted(dfs(email))
                temp = [name]
                temp.extend(path)
                res.append(temp)
        return res
        