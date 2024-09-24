import collections
from typing import List


# Question:
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and using only constant extra spaceclass Solution:

# OPTIMAL SOLUTION
# Tortoise and Hare (Cycle Detection) 
# Assumes that 1 ≤ nums[i] ≤ n
    # O(n) Time  O(1)space
    def findDuplicate(self, nums: List[int]) -> bool:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]

        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
            

        return slow
                
              
    # smaller solution # O(n) Time  O(n)space
    def findDuplicate1(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))    


    # my Solution  # O(n) Time  O(n)space
    def containsDuplicate2(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False   

     


