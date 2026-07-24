class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set() # hash 
        for num in nums:
            if num in duplicate:
                return True
            duplicate.add(num)
        return False

        