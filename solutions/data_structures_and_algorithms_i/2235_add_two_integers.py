class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2;

if __name__ == "__main__":
    s = Solution()
    res = s.sum(1,2)
    print(res == 3)