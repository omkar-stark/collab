class Solution(object):
    def twoSum(self, nums, target):
            print("Hello")
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]  # Return the indices
nums = [1,2,3,4]
target = 3

solution_inst = Solution()
output = solution_inst.twoSum(nums,target)
print(output)
