import random

def start():
    global num
    num = random.randint(1,100) 
    print('numgame')
    print(num)
    return ('숫자 게임을 시작합니다. 1부터 100 사이의 숫자를 입력해 주세요.')
    
def check(ans):
    global num
    if ans<num:
        return(f'{ans}보다 큽니다.')
    elif ans>num:
        return(f'{ans}보다 작습니다.')
    elif ans==num:
        return('정답입니다.')

def answer():
    return(f'정답은 {num}입니다.')