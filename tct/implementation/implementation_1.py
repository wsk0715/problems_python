"""
이것이 코딩 테스트다
p. 110 - 상하좌우

문제: 주어진 조건에 행동을 수행한다.

a. N x N 크기의 격자가 있다.
b. 좌상단의 좌표는 (1, 1), 우하단의 좌표는 (N, N)이다.
c. 움직일 수 있는 경우의 수는 상, 하, 좌, 우 4가지이다.
d. 이동의 결과로 격자를 벗어나게 된다면 해당 이동은 무효이다.
e. 모든 이동이 끝나고 최종적으로 위치한 좌표를 출력한다.
"""

size = int(input())
moves = input().split()

# 초기 위치
[pos_x, pos_y] = [1, 1]

directions = ['R', 'L', 'U', 'D']  # 이동할 수 있는 방향
# 각 방향 별 이동량
move_y = [0, 0, -1, 1]
move_x = [1, -1, 0, 0]

for move in moves:  # 입력한 방향 각각에 대해
    for i in range(len(directions)):  # 이동할 수 있는 방향에 대해
        if move == directions[i]:  # 입력한 방향과 이동 방향이 일치하면
            new_x = pos_x + move_x[i]  # x좌표 계산
            new_y = pos_y + move_y[i]  # y좌표 계산
    if new_y < 1 or new_y >= size or new_x < 1 or new_x >= size:
        continue  # 공간을 벗어났다면, 계산 반영하지 않음
    [pos_x, pos_y] = [new_x, new_y]  # 공간을 벗어나지 않았다면 계산 반영

print(pos_y, pos_x)
