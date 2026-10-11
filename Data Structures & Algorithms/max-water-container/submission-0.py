class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_container = 0
        left_i = 0
        right_i = len(heights)-1
        while left_i < right_i:
            bar_distance = right_i - left_i
            height = min(heights[left_i], heights[right_i])
            container = height* bar_distance
            if container > max_container:
                max_container = container
            if heights[left_i] < heights[right_i]:
                left_i += 1
            else:
                right_i -= 1
        return max_container
