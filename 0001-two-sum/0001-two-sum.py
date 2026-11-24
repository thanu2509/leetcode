class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            num=nums[i]
            for j in range(i+1,len(nums)):
                if num+nums[j]==target:
                    return [i,j]

        