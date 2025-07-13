from collections import defaultdict
class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        row_indegree = [0]*(k+1)
        col_indegree = [0]*(k+1)
        row = defaultdict(list)
        col = defaultdict(list)
        res = [[0]*k for _ in range(k)]

        for abv,bel in rowConditions:
            row[bel].append(abv)
            row_indegree[abv] += 1
        
        for left,right in colConditions:
            col[right].append(left)
            col_indegree[left] += 1
        
        def has_cycle(node, graph, state):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
            
            state[node] = 1
            for nei in graph[node]:
                if has_cycle(nei,graph,state):
                    return True
            state[node] = 2
            return False
       # print("this is row")
        #print(row)
        #print(col)
        # Cycle detection
        state_row = [0] * (k + 1)
        state_col = [0] * (k + 1)
        for i in range(1,k+1):
            if state_row[i] == 0:
                if has_cycle(i,row,state_row):
                    return []
            if state_col[i] == 0:
                if has_cycle(i,col,state_col):
                    return []

        row_queue = deque()
        for i in range(1,k+1):
            if row_indegree[i] == 0:
                row_queue.append(i)
        
        col_queue = deque()
        for i in range(1,k+1):
            if col_indegree[i] == 0:
                col_queue.append(i)
        
        insert_row_seq = []
        while row_queue:
            node = row_queue.popleft()
            insert_row_seq.append(node)

            if node in row:
                for nei in row[node]:
                    row_indegree[nei] -= 1
                    if row_indegree[nei] == 0:
                        row_queue.append(nei)
        #print(insert_row_seq)
        
        insert_col_seq = []
        while col_queue:
            node = col_queue.popleft()
            insert_col_seq.append(node)

            if node in col:
                for nei in col[node]:
                    col_indegree[nei] -= 1
                    if col_indegree[nei] == 0:
                        col_queue.append(nei)
        #print(insert_col_seq)
       
        val = [(-1,-1)]*(k+1)
        start_row = k - 1
        assigned_row = set()
        for i in range(len(insert_row_seq)):
            assigned_row.add(insert_row_seq[i])
            val[insert_row_seq[i]] = (start_row,0)
            start_row -= 1
        
        start_col = k - 1
        assigned_col = set()
        for j in range(len(insert_col_seq)):
            assigned_col.add(insert_col_seq[j])
            val[insert_col_seq[j]] = (val[insert_col_seq[j]][0], start_col)
            start_col -= 1

        if start_row >= 0:
            for i in range(1,k+1):
                if i not in assigned_row:
                    val[i] = (start_row,val[i][1])
                    start_row -= 1
                    assigned_row.add(i)

        if start_col >= 0:
            for i in range(1,k+1):
                if i not in assigned_col:
                    val[i] = (val[i][0],start_col)
                    start_col -= 1
                    assigned_col.add(i)

        for i in range(1,k+1):
            x,y = val[i]
            res[x][y] = i
        return res
