class Solution:
    def reverse(self, x: int) -> int:
        rev = int(("-" if x < 0 else "") + str(x if x > 0 else -x)[::-1])
        return rev if rev < 2**31 - 1 and rev > -(2**31) else 0