# 1)	Python 앱이 시작되면 환영인사 출력
# 2)	취존이 어떤 문장의 줄임말인가요? 출력되고 입력받음
# 3)	입력 받은 문장과 저장된 문장을 비교해 같으면 정답 틀리면 오답출력
# 4)	3개 질문 모두 완료시 “3개 퀴즈 중 X개 정답” 출력

cnt = 0
print('-'*40)
print('🤗 줄임말 퀴즈에 오신 것을 환영합니다. 🤗')
print('-'*40)

quiz1_list = ['취향존중', '취향 존중']
quiz2_list = ['솔직히까놓고말해서', '솔직히 까놓고 말해서', '솔직히 까놓고 말하자면', '솔직히 까놓고 말하다']
quiz3_list = ['케이스 바이 케이스', '케이스바이케이스', '케이스바이 케이스', '케이스 바이케이스']

quiz1 = input('Quiz 1: <취존>이 어떤 문장의 줄임말인가요?  ')
quiz2 = input('Quiz 2: <솔까말>이 어떤 문장의 줄임말인가요?  ')
quiz3 = input('Quiz 3: <케바케>가 어떤 문장의 줄임말인가요?  ')

if quiz1 in quiz1_list:
    print('정답')
    cnt += 1
elif quiz1 not in quiz1_list:
    print('오답')
if quiz2 in quiz2_list:
    print('정답')
    cnt += 1
elif quiz2 not in quiz2_list:
    print('오답')
if quiz3 in quiz3_list:
    print('정답')
    cnt += 1
elif quiz3 not in quiz3_list:
    print('오답')

print('-'*40)
print(f'3개 퀴즈 중 {cnt}개 정답')
print('-'*40)
