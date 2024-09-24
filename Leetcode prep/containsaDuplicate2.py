class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for i, n in enumerate(nums):
            if n in index_map and abs(i - index_map[n])<=k:
                return True
            index_map[n] = i
        return False 

        