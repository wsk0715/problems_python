# 이것이 코딩 테스트다
# p.92 - 2. 큰 수의 법칙

# 문제: 주어진 조건에 따라 수를 더한다.
# 가장 큰 수가 나오려면 어떻게 해야 하는가?

# a. 가장 큰 수를 K번 더한다.
# b. 다음으로 큰 수를 한 번 더한다.
# c. 반복한다.


# N개의 수에서
# M번 더한다
# 한번에 K번까지 연속될 수 있다
[N, M, K] = list(map(int, input().split()))
numbers = list(map(int, input().split()))

# 1. 가장 큰 수를 찾는다.
numbers.sort()
first = numbers[-1]

# 2. 두 번째로 큰 수를 찾는다.
second = numbers[-2]

# 3. 가장 큰 수를 계속 더한다.
# 4. 연속으로 K번 더했다면 그 다음 수를 중간에 한 번 더한다.
# 5. M번 더할 때까지 반복한다.
result = 0
dup = 0
for i in range(0, M):
    if (dup == K):
        dup = 0
        result += second
        continue
    result += first
    dup += 1

print(result)
