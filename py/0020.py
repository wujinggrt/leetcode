class Solution:
    def checkTop(self, l: List[str], p: str):
        if len(l) == 0:
            return False
        tmp = l.pop()
        return tmp == p

    def isValid(self, s: str) -> bool:
        p = list()
        for c in s:
            if c == ")":
                if not self.checkTop(p, "("):
                    return False
            elif c == "]":
                if not self.checkTop(p, "["):
                    return False
            elif c == "}":
                if not self.checkTop(p, "{"):
                    return False
            else:
                p.append(c)
        return len(p) == 0