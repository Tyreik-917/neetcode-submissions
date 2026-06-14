class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        l, r = 0, len(heights) - 1
        while l < r:

            amount = min(heights[l], heights[r]) * len(heights[l:r])

            if amount > area:
                area = amount

            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1

        return area