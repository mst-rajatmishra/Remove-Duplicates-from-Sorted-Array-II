class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        write_index = 1  # The position to write the next valid element
        count = 1        # The count of current element occurrences
        
        for read_index in range(1, len(nums)):
            if nums[read_index] == nums[read_index - 1]:
                count += 1
            else:
                count = 1  # Reset count for a new element
            
            if count <= 2:
                nums[write_index] = nums[read_index]
                write_index += 1
        
        return write_index
