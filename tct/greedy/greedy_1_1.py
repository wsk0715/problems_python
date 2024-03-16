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

# 수학적 규칙을 찾는 방법(수열)
# 1. 가장 큰 수 K개와 다음으로 큰 수 하나를 더한다.
numbers.sort()
first, second = [numbers[-1], numbers[-2]]
sum = first * K + second

# 2. 이것을 M을 K+1로 나눈 값만큼 곱한다.
times = M // (K + 1)
result = sum * times

# 3. 나머지만큼 다시 가장 큰 수를 더한다.
extra = M % (K + 1)
result += first * extra
print(result)
