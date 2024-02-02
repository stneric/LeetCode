class Solution:
    def sequentialDigits(self, low, high):
        result = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(1, 10 - length + 1):
                num = int("".join(str(x) for x in range(start, start + length)))
                if low <= num <= high:
                    result.append(num)
                elif num > high:
                    break
        return result

if __name__ == '__main__':
    print(Solution().sequentialDigits(10, 1000000))
