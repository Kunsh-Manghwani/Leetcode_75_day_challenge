class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        i = 0
        j=0
        while j<len(nums):
            if nums[i]!=nums[j]:
                i = i+1
                nums[i] = nums[j]
            j = j+1
        return i+1