class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        p=[]
        for i in tokens:
            if i=='+' or i=='-' or i=='*' or i=='/' :
                x=int(p.pop())
                y=int(p.pop())
                match i:
                    case '+':
                        p.append(x+y)
                    case '-':
                        p.append(y-x)
                    case '*':
                        p.append(x*y)
                    case '/':
                        p.append(y/x)
            else:
                p.append(i)
        print(p)
        return int(p[0])