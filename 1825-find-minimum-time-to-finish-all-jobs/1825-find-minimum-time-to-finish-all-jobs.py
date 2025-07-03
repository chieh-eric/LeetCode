class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        worker = [0]*k
        self.min_time = float('inf')
        n = len(jobs)
        jobs.sort(reverse=True)
        def backtrack(i):
            if i == n:
                self.min_time = min(self.min_time, max(worker))
                return
            
            for j in range(k):
                worker[j] += jobs[i]
                if self.min_time > worker[j]:
                    backtrack(i+1)
                
                worker[j] -= jobs[i]
                if worker[j] == 0:
                    break
        backtrack(0)
        return self.min_time