class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        z = list(accumulate(nums))
        a = 0
        mx = z[-1]
        #print(mx)
        if len(nums)==1 or mx-nums[0] == 0:
            return 0
        for i in range(1,len(nums)):
            a = z[i-1]
            #print(a,mx-z[i])
            if a==mx-z[i]:
                return i
        return -1
        