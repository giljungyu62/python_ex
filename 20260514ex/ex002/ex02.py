# flag = True

# members ={}

# while flag:
#     selectedMenuNum = int(input('1.회원가입           2. 프로그램 종료'))

#     if selectedMenuNum == 1:
#         id = input('아이디: ')
#         pw = input('비밀번호: ')
#         members[id] = pw

#     elif selectedMenuNum == 2:
#         flag = False

#         for key in members.keys():
#             print(f'ID: {key}, PW: {members[key]}')

# classes =  {'python':'5학점', 'C/C++':'5학점', 'HTML5':'5학점', 
#             'Java':'5학점', 'Javascript':'5학점'}


# for key in classes:
#     if classes[key] == '3학점':
#         classes[key] == '5학점'

# print(classes)


'''
members = {
    '2019-052001': ['박찬호', 25, 'M', '010-1234-5678', '헬스, 수영', 0],
    '2019-052004': ['박용택', 65, 'M', '010-9012-3456', '수영', 50],
    '2019-052003': ['박세리', 70, 'W', '010-7890-1234', '아쿠아로빅', 50]
}

# 전체 회원 정보 출력
for key in members:
    print(f'회원번호: {key}, 회원정보:{members[key]}')

print('-' * 30)

# 전체 회원 정보 출력을 하는데, 이떄 회원의 '이름'과 '성별'만 출력을 하자!
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value[0]},{value[2]}')
'''

members = {
    '2019-052001': {
        '이름': '박찬호',
        '나이': 25,
        '성별': 'M',
        '연락처': '010-1234-5678',
        '이용서비스': ['헬스', '수영'],
        '할인율': 0
    },
    '2019-052004': {
        '이름': '박용택',
        '나이': 65,
        '성별': 'M',
        '연락처': '010-9012-3456',
        '이용서비스': ['수영'],
        '할인율': 50
    },
    '2019-052003': {
        '이름': '박세리',
        '나이': 70,
        '성별': 'W',
        '연락처': '010-7890-1234',
        '이용서비스': ['아쿠아로빅'],
        '할인율': 50
    }
}

# 전체 회원 정보 출략
for key in members:
    print(f'회원번호: {key}, 회원정보:{members[key]}')

print('-' * 30)

# 전체 회원 정보 출력을 하는데, 이떄 회원의 '이름'과 '성별'만 출력을 하자!
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']},{value['성별']}')

print('-' * 30)

# 전체 회원 정보 출력을 하는데, 이떄 회원의 '이름', '성별' 그리고 '이용서비스' 그리고 이용서비스개수 만 출력을 하자!
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}, {value['이용서비스']}, {len(value['이용서비스'])}')

vegetables = {}
vegetables["당근"] = 10
vegetables["건대추"] = 100
vegetables["대파"] = 20
vegetables["애호박"] = 3
vegetables["부추"] = 1
vegetables["당근"] -= 1
vegetables["건대추"] -= 10
vegetables["대파"] -= 1
vegetables["애호박"] -= 1
vegetables["부추"] -= 1

print('야채별 재고 현황')
print('-' * 30)

for vegetable, count in vegetables.items():
    print(f'{vegetable}: {count}')

# :: 용돈 기입장 :::::
from datetime import datetime

MENU_INCOME     = 1
MENU_EXPENSE    = 2
MENU_VIEW       = 3
EXIT            = 99

flag = True
DEV_MOD = True

bankAccount = []
currentMoney = 0

if DEV_MOD:
    txt =  '[2026-05-15 15:14:08] \t 100 \t\t aaaaa \t\t 100'
    bankAccount.append(txt)
    txt = '[2026-05-15 15:15:08] \t 200 \t\t bbbbb \t\t 300'
    bankAccount.append(txt)
    txt = '[2026-05-15 15:16:08] \t\t -50 \t ccccc \t\t 250'
    bankAccount.append(txt)

while flag:

    selectedMenuNum = int(input('1.수입    2.지출    3.조회    99.시스템종료 -----> '))
    if selectedMenuNum == MENU_INCOME:
        incomeMoney = int(input('수입 금액: '))
        incomeDesc = input('수입 내용: ')
        currentMoney += incomeMoney

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txt = f'[{now}] \t {incomeMoney} \t {incomeDesc} \t\t\t {currentMoney}'
        bankAccount.append(txt)

    elif selectedMenuNum == MENU_EXPENSE:
        expenseMoney = int(input('지출 금액: '))
        expenseDesc = input('지출 내용: ')
        currentMoney -= expenseMoney

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txt = f'[{now}] \t\t\t -{expenseMoney} \t {expenseDesc} \t {currentMoney}'
        bankAccount.append(txt)

    elif selectedMenuNum == MENU_VIEW:
        print('-' * 63)
        print('날짜&시간 \t\t 입금 \t 출금 \t 내역 \t\t 잔액')
        print('-' * 63)
        for item in bankAccount:
            print(item)
        print('-' * 63)

    elif selectedMenuNum == EXIT:
        flag = False 






