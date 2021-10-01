class Solution:
    def firstMissingPositive(self, numbers) -> int:
        has1 = 0
        for i in range(len(numbers)):
            if(numbers[i] == 1):
                has1 = True
            if(numbers[i] < 0):
                numbers[i] = 0

        if not has1:
            return 1

        for i in range(len(numbers)):
            if(abs(numbers[i]) > 0 and abs(numbers[i]) <= len(numbers)):
                if(numbers[abs(numbers[i]) - 1] == 0):
                    numbers[abs(numbers[i]) - 1] = -1
                elif(numbers[abs(numbers[i]) - 1] > 0):
                    numbers[abs(numbers[i]) - 1] *= -1

        for i in range(len(numbers)):
            if numbers[i] >= 0:
                return i + 1

        return len(numbers) + 1
