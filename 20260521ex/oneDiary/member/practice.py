# s = 0

# for i in range(5):
#     n = int(input('n:'))
#     s = s + n

# print('합:',s)
# print('평균:',s/5)

# n = int(input('n: '))

# for i in range(1, 10):
#     print('{}*{} = {}'. format(n, i, n * i))

# li = ['a','d','e','b','c']

# for i in range(len(li)-1,-1,-1):
#     print(li[i])

# for j in range(2,10):
#     for i in range(1,10):
#         print('{}*{}={}'.format(j,i,j*i))
#     print()

# a, b = map(int,input('시작단 끝단 입력: ').split())

# for j in range(a,b+1):
#     for i in range(1,10):
#         print('{}*{} = {}'.format(j,i,j*i))
#     print()

# for i in range(1,7):
#     for j in range(1,7):
#         print(i,j)  

# for i in range(1,11):
#     if i == 5:
#         break
#     print(i, end = '')

# n = int(input('n: '))
# for i in range(1, n+1):
#     if i % 3 == 0:
#         continue
#     print(i,end = '')

# n = int(input('n: '))
# i = 0
# while True:
#     i = i + 1
#     print(i, end ='')
#     if i == n:
#         break

# li = [7,4,3,2,6,5,9,1,8,10]
# n = int(input('1~10: '))

# for i in li:
#     print(i, end='')
#     if n == i:
#         break
# def func1():
#     print('hi~')
# def func2(n):
#     print(n * 2)
# def func3():
#     n = int(input('n: '))
#     return n * 2
def func4(x,y):
    return x+y
print(func4(5,7))