class Solution:
    @staticmethod
    def solve(s: str) -> int:

        total = 0
        for i in range(len(s)):
            if s[i].isdigit():
                total += int(s[i])
        return total

if __name__ == "__main__":
    s: str = input()
    print(Solution.solve(s))