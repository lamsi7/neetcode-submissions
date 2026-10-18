class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_i = 0
        right_i = len(nums) - 1
        while left_i <= right_i:
            mid_i = right_i - left_i // 2
            if nums[mid_i] == target:
                return mid_i
            elif nums[mid_i] < target:
                left_i = mid_i + 1
            else:
                right_i = mid_i - 1
        return -1
        