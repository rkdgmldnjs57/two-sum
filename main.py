from typing import List
def twoSum(self, nums: List[int], target: int) -> List[int]:
    # YOUR ANSWER
    for i in range(len(nums)): 
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]

print(twoSum(0, [3,3], 6))