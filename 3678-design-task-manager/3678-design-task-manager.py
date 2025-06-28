import heapq
class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        self.heap = [] # maxHeap for highest priority value, value = (priority, taskId, userId)
        self.curPrior = {} # Key = task, Val = priority 
        self.taskUserMap = {}

        for user, task, pri in tasks:
            self.curPrior[task] = pri
            heapq.heappush(self.heap,(-pri,-task,user))
            self.taskUserMap[task] = user


        

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        heapq.heappush(self.heap,(-priority,-taskId,userId))
        self.taskUserMap[taskId] = userId 
        self.curPrior[taskId] = priority

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        userId = self.taskUserMap[taskId]
        heapq.heappush(self.heap,(-newPriority,-taskId,userId))
        self.curPrior[taskId] = newPriority

        

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        del self.curPrior[taskId]
        del self.taskUserMap[taskId]
 
    def execTop(self):
        """
        :rtype: int
        """
       
        while self.heap and ((-self.heap[0][1]) not in self.curPrior or self.curPrior[-self.heap[0][1]] != -self.heap[0][0] or (-self.heap[0][1]) not in self.taskUserMap or self.taskUserMap[-self.heap[0][1]] != self.heap[0][2]):
          
            heapq.heappop(self.heap)

        if not self.heap:
            return -1
        
        _, neg_task, userId = heapq.heappop(self.heap)
        taskId = -neg_task
        del self.curPrior[taskId]
        del self.taskUserMap[taskId]

        return userId



# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()