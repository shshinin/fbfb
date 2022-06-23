# 숫자가 3의 배수이면 fizz를 출력
# 숫자가 5의 배수이면 buzz를 출력
# 숫자가 15의 배수이면 fizzbuzz를 출력
# 숫자의 범위는 1~45

for i in range(1, 45 + 1):
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
