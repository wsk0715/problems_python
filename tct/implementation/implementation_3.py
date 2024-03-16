"""
이것이 코딩 테스트다
p.115 - 2). 왕실의 나이트

문제: 주어진 조건에 따라 행동한 후, 결과를 출력한다.

a. 8x8 좌표 평면으로 이루어진 정원이 있다.
b. 좌표 평면의 행은 (1 ~ 8), 열은 (a ~ h)로 나타내진다.
c. 나이트는 다음과 같이 행동할 수 있다.
    1. 수평으로 두 칸 이동한 뒤, 수직으로 한 칸 이동
    2. 수직으로 두 칸 이동한 뒤, 수평으로 한 칸 이동
    3. 나이트는 정원 밖으로 나갈 수 없다.
d. 나이트의 현재 위치를 입력받아, 이동할 수 있는 경우의 수를 출력한다.
"""

pos = input()

cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
cols_value = ['1', '2', '3', '4', '5', '6', '7', '8']
rows_value = ['1', '2', '3', '4', '5', '6', '7', '8']

pos = [pos[0], pos[1]]  # 입력을 열과 행으로 분리
for i in range(len(cols)):
    if pos[0] == cols[i]:
        pos[0] = cols_value[i]  # 알파벳을 열에 해당하는 숫자로 변경
pos = list(map(int, pos))

[move_y1, move_x1, move_y2, move_x2] = [[2, -2], [1, -1], [1, -1], [2, -2]]
count = 0
for i in range(4):
    for j in range(len(move_y1)):  # c-1번 움직임 계산: 수평2, 수직1
        new_pos_y = pos[1] + move_y1[i]
        new_pos_x = pos[0] + move_x1[j]
        if 1 <= new_pos_y <= 8 and 1 <= new_pos_x <= 8:  # 계산 결과, 정원 안에 있으면 +1
            count += 1
    for j in range(len(move_y2)):  # c-2번 움직임 계산: 수직1, 수평2
        new_pos_y = pos[1] + move_y2[i]
        new_pos_x = pos[0] + move_x2[j]
        if 1 <= new_pos_y <= 8 and 1 <= new_pos_x <= 8:  # 계산 결과, 정원 안에 있으면 +1
            count += 1
print(count)
