class Solution:
    def isPalindrome(self, s: str) -> bool:
        len_of_str = len(s)
        left_i = 0
        right_i = len_of_str - 1
        while left_i < right_i:
            if not (s[left_i].lower().isalnum()):
                left_i +=1
                continue
            elif not (s[right_i].lower().isalnum()):
                right_i -=1
                continue
            if s[left_i].lower() == s[right_i].lower():
                left_i +=1
                right_i -= 1
            else:
                return False
        return True
            
        