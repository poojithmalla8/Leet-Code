class Solution:
    def isValid(self, s: str) -> bool:
        smap = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in smap:
                stack.append(c)
                continue
            if not stack or stack[-1] != smap[c]:
                return False
            stack.pop()

        return True if not stack else False