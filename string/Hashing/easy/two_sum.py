class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## inefficient. Brute force
        # for idx, i in enumerate(nums):
        #     if (target-i) in nums:
        #         if nums.index(target-i) == idx:
        #             pass
        #         else:
        #             return [idx,nums.index(target-i)]
        hash_map = {}
        for idx, i in enumerate(nums):
            if target - i in hash_map:
                return [idx,hash_map[target-i]]
            else:
                hash_map[i] = idx