from typing import List


class Solution:
    @staticmethod
    def running_sum(nums: List[int]) -> List[int]:
        return [elem + sum(nums[:i]) for i, elem in enumerate(nums)]
