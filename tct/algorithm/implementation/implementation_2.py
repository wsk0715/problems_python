"""
이것이 코딩 테스트다
p.113 - 시각

문제: 주어진 조건에 따라 결과를 출력한다.

a. 정수 N을 입력받는다.
b. 00시 00분 00초부터 N시 59분 59초까지의 시각 중,
    3이 하나라도 포함되는 시각의 경우의 수를 출력한다.
"""

N = int(input())

# 00:00:00 - 0
# 23:59:59 - 86400
total = 3600 * (N + 1) - 1
result = []
[H, M, S] = [0, 0, 0]
for i in range(total):
    S += 1
    if S == 60:
        S = 0
        M += 1
    if M == 60:
        M = 0
        H += 1
    # 1. 시, 분, 초의 일의 자리가 3인 경우
    if S % 10 == 3 or M % 10 == 3 or H % 10 == 3:
        result.append(str([H, M, S]))
    # 2. 분, 초의 십의 자리가 3인 경우(시는 x)
    if S // 10 == 3 or M // 10 == 3:
        result.append(str([H, M, S]))
# 3. 중복을 제거
result = list(dict.fromkeys(result))  # 딕셔너리 key화, 다시 list화
print(len(result))
