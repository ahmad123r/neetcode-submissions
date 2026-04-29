class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if len(nums) ==0:
            return False
        hash_map = {}
        for x in nums:
            hash_map[x] = 0

        for j in nums:
            hash_map[j] += 1
        if max(hash_map.values()) > 1:
            return True
        return False