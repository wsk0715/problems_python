# 이것이 코딩 테스트다
# p.96 - 3. 숫자 카드 게임

# 문제: 규칙을 지키며 가장 큰 숫자의 카드를 뽑아야 한다.

# a. N행 x M열에 카드가 하나씩 놓여져 있다.
# b. 먼저, 뽑고자 하는 카드가 포함된 행을 선택한다.
# c. 그 다음, 선택된 행에서 가장 낮은 숫자의 카드를 뽑는다.
# d. 이 규칙을 지키며, 가장 높은 숫자의 카드를 뽑는다.


# N x M 공간이 있다.
[N, M] = list(map(int, input().split()))
# 카드 목록을 입력한다.
field = []
for i in range(0, N):
    field.append(list(map(int, input().split())))

# 1. 각 행에서 최소값을 구한다.
min_values = []
for row in field:
    min_values.append(min(row))

# 2. 최소값들 중 가장 큰 값의 카드의 값을 구한다.
for val in min_values:
    max_value = max(min_values)
print(max_value)
