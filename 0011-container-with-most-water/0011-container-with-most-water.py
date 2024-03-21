class Solution:
    def maxArea(self, height: List[int]) -> int:
        capacity = 0
        left,right = 0,len(height)-1
        while left < right:
            count = min(height[left],height[right])
            capacity = max(capacity,count * (right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return capacity