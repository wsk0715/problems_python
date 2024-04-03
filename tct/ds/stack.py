stack = []  # 빈 스택

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)  # 아래서부터, 5
stack.append(2)  # 5, 2
stack.append(3)  # 5, 2, 3
stack.append(7)  # 5, 2, 3, 7
stack.pop()  # 5, 2, 3
stack.append(1)  # 5, 2, 3, 1
stack.append(4)  # 5, 2, 3, 1, 4
stack.pop()  # 5, 2, 3, 1

print(stack)  # (순서대로) 최하단 원소부터 출력, [5, 2, 3, 1]
print(stack[::-1])  # (거꾸로) 최상단 원소부터 출력, [1, 3, 2, 5]
