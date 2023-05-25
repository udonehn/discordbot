import random

def start():
    global num
    while True:
        num = random.randint(101,1000)
        if check_zero(str(num)) or check_duplicate(str(num)):
            continue
        num=str(num)
        break
    print('baseball')
    print(num)
    return ('숫자야구를 시작합니다. 숫자를 입력해 주세요.')
    
def check(ans):
    global num
    if not check_letter(ans):
        return('자리수가 올바르지 않습니다.')
    
    if check_duplicate(ans):
        return('모두 다른 숫자여야 합니다.')
    
    if ans==num:
        return('정답입니다.')
        
    strike,ball=0,0
    for j in range(len(ans)):
        for k in range(len(ans)):
            if num[j]==ans[k]:
                if j==k:
                    strike+=1
                else:
                    ball+=1
    return((f'{strike}스트라이크 {ball}볼 입니다.'))                
    
    
def check_letter(ans):
    global num
    if len(ans)==len(num):
        return True
    else:
        return False
    
def check_zero(num):
    for i in list(num):
        if i=='0':
            return True
    return False

def check_duplicate(num):
    for i in range(len(num)):
        for j in range(len(num)):
            if num[i]==num[j] and i!=j:
                return True
    return False

def answer():
    global num
    return(f'정답은 {num}입니다.')