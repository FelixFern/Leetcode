class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_position = 0

        if (len(nums) == 1):
            return True

        if (nums[0] == 0 and len(nums) > 1):
            return False

        while curr_position <= len(nums) - 1:
            max_jump = -1
            temp_position = curr_position

            if (curr_position + nums[curr_position] >= len(nums) - 1):
                return True

            for i in range(curr_position + 1, curr_position + nums[curr_position] + 1):
                if ((nums[i] >= max_jump and i >= temp_position) or (max_jump + temp_position <= i)):
                    max_jump = nums[i]
                    temp_position = i

            if (max_jump == 0):
                return False

            curr_position = temp_position

        return True
