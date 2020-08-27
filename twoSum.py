class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_array=[]
        n=len(nums)
        for i in range(0,n):
        

                searchNum=target-nums[i]


                if searchNum in nums:
                    j=nums.index(searchNum)
                    if(i!=j):
                        first = i
                        final_array=[j,i]
                        return(final_array)
