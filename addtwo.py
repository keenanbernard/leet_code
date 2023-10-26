class Solution(object):

    def addTwoNumbers(self, l1, l2):
        one = []
        two = []

        l1_index = [i for i, e in sorted(enumerate(l1))]
        l2_indexes = [i for i, e in sorted(enumerate(l2))]
        l1_index.sort(reverse=True)
        l2_indexes.sort(reverse=True)

        for i in l1_index:
            one.append(l1[i])

        for i in l2_indexes:
            two.append(l2[i])

        return one, two


sol = Solution()
result = sol.addTwoNumbers([2, 4, 3], [5, 6, 4])
print(result)
