import random

rnd_val = random.randint(1, 20)
is_end = False


# function
def compare_val(i1):
    if i1 == rnd_val:
        print('정답')
        return True
    elif i1 > rnd_val:
        print('다운')
        return False
    else:
        print('업')
        return False


print(rnd_val)  # 디버그


# loop 3 times
for i in range(3, 0, -1):
    i1 = int(input('숫자를 맞춰보세요'))
    ret = compare_val(i1)
    if ret:
        break
    print('기회가 ' + str(i - 1) + '번 남음')
