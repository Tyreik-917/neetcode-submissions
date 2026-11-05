class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        l, r = 0, len(heights) - 1
 
        while l < r:
            amount = min(heights[l], heights[r]) * (r-l)

            if amount > area:
                area = amount

            if heights[l] < heights[r]:
                l+=1

            else:
                r-=1

        return area

        