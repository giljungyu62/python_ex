# split(쪼갠다.)
'''
names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')
print(f'names: {names}')
print(f'names type: {type(names)}')

str = "박찬호 이승엽 박세리 박지성 이순철 선동열 손흥민 김연아"
splitedStr = str.split(" ")  # list-> tuple
print(f'splitedStr: {(splitedStr)}')
print(f'splitedStr type: {type(splitedStr)}')

str = "박찬호+이승엽+박세리+박지성+이순철+선동열+손흥민+김연아"
splitedStr = str.split("+")   # list

splitedStr = tuple(splitedStr)
print(f'splitedStr:{splitedStr}')
print(f'splitedStr type:{type(splitedStr)}')
'''
# a, b = input('두 개의 정수를 입력하세요: ').split(",")     # 3,5 > [3, 5]

# # a, b = [3, 5]
# print(a)
# print(b)

# 활당(대인) 연산
num = 10

# 구조분해할당
# [1, 2]> a = 1, b = 2

# nums = [1, 2]
# a = nums[0]
# b = nums[1]

# a, b = [1, 2]  # a = 1, b = 2
# print(a)
# print(b)

# x, y = (10, 20)
# print(x)
# print(y)

# a = 1
# b = 2
# a, b = b, a

# a, *rest = [1, 2, 3, 4]
# '''
# a = 1
# rest = [2, 3, 4]
# '''
a = 10
b = 1.2
c = 'hello'

a = float(a)
b = int(b)

print(type(a))
print(type(b))
print(type(c))