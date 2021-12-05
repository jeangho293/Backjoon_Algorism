N = int(input())

first_number, increase_number = 5, 7    # 첫번재 도형, 첫번째로 증가하는 숫자

for i in range(1, N):
    first_number += increase_number
    increase_number += 3    # 규칙상 7, 10, 13, 16 ... 으로 증가하는 등차수열

print(first_number % 45678)