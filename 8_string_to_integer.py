import re

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = re.findall('(^[\+\-0]*\d+)\D*', str.strip())
        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0


if __name__ == '__main__':
    str = " -42 "
    solution = Solution()
    ans = solution.myAtoi(str)
    print(ans)