s = input()

stack = []
closeToOpen = {')':'(', '}':'{',']':'['}

for i in s:
    if i in closeToOpen:
        if stack and stack[-1] == closeToOpen[i]:
            stack.pop()
        else:
            print(False)
    else:
        stack.append(i)

print(True if not stack else False)
    