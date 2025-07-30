from collections import defaultdict
class Solution(object):
    def minJumps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = max(nums)
        is_prime = [True]*(total + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2,int(total**0.5)+1):
            if is_prime[i]:
                for j in range(i*i,total+1,i):
                    is_prime[j] = False


        val__to_index = defaultdict(list)
        for i, num in enumerate(nums):
            val__to_index[num].append(i)
        
        dis_to_index = defaultdict(set)

        for val in val__to_index:
            for p in range(2,int(val**0.5)+1):
                if val % p == 0:
                    if is_prime[p]:
                        dis_to_index[p].update(val__to_index[val])
                    q = val // p
                    if is_prime[q]:
                        dis_to_index[q].update(val__to_index[val])
            if is_prime[val]:
                dis_to_index[val].update(val__to_index[val])
        #print(val__to_index)
        #print(dis_to_index)
        n = len(nums)
        queue = deque([(0, 0)])
        visited = [False]*n
        used = set()
        while queue:
            #print(queue)
            #print(queue)
            index, step = queue.popleft()
            if index == n - 1:
                return step
                
            if visited[index]:
                continue

            if index - 1 >= 0 and not visited[index-1]:
                queue.append((index-1, step+1))
            
            if index + 1 < n and not visited[index+1]:
                queue.append((index+1,step+1))

            visited[index] = True
            #print(queue)
            if is_prime[nums[index]] and nums[index] not in used:
                for i in dis_to_index.get(nums[index],[]):
                    if not visited[i]:
                        used.add(nums[index])
                        queue.append((i,step+1))
        return -1
        