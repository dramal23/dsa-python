class Solution:
    def twoSumBruteForce(self, array, target: int):
        for i in range(len(array)):
            for j in range(i+1, len(array)):
                if array[i] + array[j] == target:
                    return [i, j]
        return []