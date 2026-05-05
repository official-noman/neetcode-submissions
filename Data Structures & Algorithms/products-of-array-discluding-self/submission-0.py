class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Result array ke prothome 1 diye faka kore nilam
        res = [1] * n 
        
        # Step 1: Bam theke Dan e (Prefix pass)
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i] # Porer index er jonno prefix update korlam
            
        # Step 2: Dan theke Bam e (Postfix pass)
        postfix = 1
        # range(n-1, -1, -1) mane holo ekdom last index theke 0 porjonto ulta loop
        for i in range(n - 1, -1, -1):
            res[i] *= postfix # Aager prefix er sathe ekhonkar postfix gun kore dilam
            postfix *= nums[i] # Porer index er jonno postfix update korlam
            
        return res
        