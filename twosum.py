class Solution:
    def twoSum(self, nums, target):
        count = 0
        solution = []

        for index, num1 in enumerate(nums):
            for ind, num2 in enumerate(nums):
                if index == ind:
                    break
                if num1 + num2 == target:
                    count += 1
                    solution.append(index)
                    solution.append(ind)

                    break

            if count == 1:
                break

        solution.sort()
        return solution


sol = Solution()
result = sol.twoSum([3, 3], 6)
print(result)
