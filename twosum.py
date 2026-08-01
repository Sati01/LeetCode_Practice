class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use a hashmap to store the numbers and their indices
        #Your Code Here
        itmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in itmap:
                return [itmap[diff], i]
            itmap[n] = i   


        