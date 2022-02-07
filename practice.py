# # 참 / 거짓 (boolean)
# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))

# 애완동물을 소개해 주세요~
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

# '''
# 이렇게 하면 
# 여러문장이
# 주석처리
# 됩니다'''

# # contrl + / 누르면 전체주석처리
# print("우리집 " + animal + "의 이름은 " + name + "예요")
# hobby = "공놀이"
# #print(name + "는" + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name, "는", age, "살이며, ", hobby, "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult) )

# print(1+1) # 2
# print(3-2) # 1
# print(5*2) # 10
# print(6/3) # 2

# print(2**3) # 2^3 = 8
# print(5%3) # 나머지 구하기 2
# print(10%3) # 1
# print(5//3) # 몫 1
# print(10//3) # 3

# print(10 > 3) # True
# print(4 >= 7) # False
# print(10 < 3) # False
# print(5 <= 5) # True

# print(3 == 3) # True
# print(4 == 2) # False
# print(3 + 4 == 7) # True

# print(1 != 3) # True
# print(not(1 != 3)) # False

# print((3 > 0) and (3 < 5)) # True
# print((3 > 0) & (3 < 5)) # True

# print((3 > 0) or (3 > 5)) # True
# print((3 > 0) | (3 > 5)) # True

# print(5 > 4 > 3) # True
# print(5 > 4 > 7) # False

# print(2 + 3 * 4) # 14
# print((2+3) * 4) # 20
# number = 2 + 3 * 4 # 14
# print(number)
# number = number + 2 # 16
# print(number)
# number += 2 # 18
# print(number)
# number *= 2 # 36
# print(number)
# number /= 2 # 18
# print(number)
# number -= 2 # 16
# print(number)

# number %= 5 # 1
# print(number)

# print(abs(-5)) # 절댓값 5
# print(pow(4, 2)) # 4^2 = 4*4 = 16 (제곱)
# print(max(5, 12)) # 12
# print(min(5, 12)) # 5
# print(round(3.14)) # 3
# print(round(4.99)) # 5

# from math import *
# print(floor(4.99)) # 내림, 4
# print(ceil(3.14)) # 올림, 4
# print(sqrt(16)) # 제곱근, 4

# from random import *

# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성

# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)