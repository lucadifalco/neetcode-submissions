class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for i in range(len(nums)):
            num = nums[i]
            if num in hash_set:
                return True
            hash_set.add(num)
        return False