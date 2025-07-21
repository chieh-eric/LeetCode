import bisect
class TweetCounts(object):

    def __init__(self):
        self.dic = {}

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        if tweetName not in self.dic:
            self.dic[tweetName] = SortedList()
        self.dic[tweetName].add(time)
        

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        if tweetName not in self.dic:
            return []

        if freq == "minute":
            chunk_size = 60
            
        elif freq == "hour":
            chunk_size = 3600
        else:
            chunk_size = 86400

        n = (endTime - startTime + chunk_size) // chunk_size
        res = [0]*n
        left = bisect.bisect_left(self.dic[tweetName],startTime)
        for i in range(n):
            chunk_start = i*chunk_size + startTime
            chunk_end = min(chunk_start + chunk_size - 1, endTime)
            right = bisect.bisect_right(self.dic[tweetName],chunk_end)
            res[i] = right-left
            left = right
        return res



# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)