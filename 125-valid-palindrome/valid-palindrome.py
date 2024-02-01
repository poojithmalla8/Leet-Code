class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        newstr=''
        for element in s:
            if element.isalpha() or element.isalnum():
                newstr+=element
        # print(newstr)
        return (newstr == newstr[::-1])