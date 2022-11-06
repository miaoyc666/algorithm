
class Solution:
    def interpret(self, command: str) -> str:
        res = []
        for i, c in enumerate(command):
            if c == 'G':
                res.append(c)
            elif c == '(':
                res.append('o' if command[i + 1] == ')' else 'al')
        return ''.join(res)
