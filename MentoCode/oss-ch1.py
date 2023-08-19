s1 = '취향입니다존중해주세요'
s2 = '솔직히까놓고말해서'
s3 = '케이스바이케이스'
trial = 0

print('안녕하세요. 신조어 퀴즈')
i1 = input('취존은 무엇입니까?')
if i1.replace(' ', '') == s1:
    trial = trial + 1
    print('정답')
else:
    print('오답')

i2 = input('\n솔까말은 무엇입니까?')
if i2.replace(' ', '') == s2:
    trial = trial + 1
    print('정답')
else:
    print('오답')

i3 = input('\n케바케 무엇입니까?')
if i3.replace(' ', '') == s3:
    trial = trial + 1
    print('정답')
else:
    print('오답')

print('3개 중 ' + str(trial) + '개 정답')
