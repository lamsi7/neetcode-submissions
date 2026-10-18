class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left_i in range(len(nums)):
            right_i = left_i + 1
            current_sum = nums[left_i] + nums[right_i]
            if current_sum == target:
                return [left_i,right_i]
            else:
                right_i +=1
                while right_i < len(nums):
                    current_sum = nums[left_i] + nums[right_i]
                    if current_sum == target:
                        return [left_i, right_i]
                    else: 
                        right_i +=1
