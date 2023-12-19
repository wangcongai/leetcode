from typing import List


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        low, high = 0, len(nums) - 1
        results = []
        while low < high:
            if nums[low] + nums[high] == target:
                results.append([nums[low], nums[high]])
                low += 1
                high -= 1
            elif nums[low] + nums[high] < target:
                low += 1
            else:
                high -= 1
        return  results


if __name__ == '__main__':
    solution = Solution()
    print(solution.pairSums(nums=[5, 6, 5, 6, 3, 8], target=11))