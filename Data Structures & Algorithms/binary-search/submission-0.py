class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower_index = 0
        upper_index = len(nums) - 1
        while upper_index >= lower_index:
            check_index = (lower_index + upper_index) // 2
            if nums[check_index] == target:
                return check_index
            elif nums[check_index] < target:
                lower_index = check_index + 1
            elif nums[check_index] > target:
                upper_index = check_index - 1
        return -1