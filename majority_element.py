class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = 1
        ans = nums[0]
        i = 1
        while i<len(nums):
            if nums[i]==ans:
                x = x+1
            else:
                x = x-1
                if x==0:
                    x=1
                    ans = nums[i+1]
                    i = i+1
            i = i+1
        return ans
                