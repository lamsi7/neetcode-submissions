class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Input: nums = [-1,0,1,2,-1,-4]
        nums.sort()
        # nums become -> [-4,-1,-1,0,1,2]
        triplets = []
        for i in range(len(nums)):
            left_i = i+1
            right_i = len(nums)-1
            if i > 0 and (nums[i] == nums[i-1]):
                continue
            if nums[i] > 0:
                break
            while left_i < right_i:
                if nums[i] + nums[left_i] + nums[right_i] == 0:
                    triplets.append([nums[i], nums[left_i], nums[right_i]])
                    left_i += 1
                    right_i -= 1
                    while left_i < right_i and (nums[left_i]== nums[left_i-1]):
                        left_i +=1
                    while left_i < right_i and (nums[right_i]== nums[right_i+1]):
                        right_i -=1   
                elif nums[i] + nums[left_i] + nums[right_i] > 0:
                    right_i -= 1
                else:
                    left_i += 1
        return triplets