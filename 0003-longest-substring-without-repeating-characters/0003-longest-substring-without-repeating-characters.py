class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subDic = {} 
        subList = []
        count = 0
        subList.append(count)
        for i in range(len(s)):
            subDic[s[i]] = 1
            count = 1
            subList.append(count)
            for j in range(i+1,len(s),1):
                if s[j] in subDic:
                    subList.append(count)
                    count = 0
                    break
                else:
                    subDic[s[j]] = 1
                    count += 1
                    subList.append(count)
            count = 0
            subDic.clear()
        return max(subList)