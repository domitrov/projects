class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer to a string
        str_x = str(x)
        
        # Check if the string is equal to its reverse
        return str_x == str_x[::-1]

solution = Solution()

ap = solution.isPalindrome(1)

print(ap)