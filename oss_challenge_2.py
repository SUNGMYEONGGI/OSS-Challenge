# 1)	Python 앱이 시작되면 “숫자를 맞춰보세요”가 출력되고 입력을 받음
# 2)	입력 값과 랜덤 숫자를 비교해 업 다운 출력 
# 3)	입력 값과 랜덤 숫자가 같으면 정답 출력
# 4)	총 3번의 기회. 3번 안에 못 맞추면 실패 출력
# 5)	입력 값과 숫자 비교는 Python 함수를 사용해 처리
# 6)	반복문을 이용해 3회 반복 처리


import random

randNum = random.randint(1, 20)
print('-'*25)
print('🤗 숫자를 맞춰보세요 🤗')
print('-'*25)

def numgame(myNum, cnt):
    while True:
        if cnt == 3:
            if randNum == myNum:
                return '정답'
            elif randNum != myNum:
                return '실패'
        if randNum > myNum:
            print('업')
            return numgame(int(input('숫자를 맞춰보세요 : ')), cnt+1)
        elif randNum < myNum:
            print('다운')
            return numgame(int(input('숫자를 맞춰보세요 :')), cnt+1)
        elif randNum == myNum:
            return '정답'

print(numgame(int(input('숫자를 맞춰보세요 : ')), 1))