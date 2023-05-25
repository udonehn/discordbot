def start():
    print('Palindrome')
    return('팰린드롬수인지 검사합니다. 숫자를 입력 해 주세요.')
        
def check(ans):
    text = list(ans)
    
    if len(text) == 1:
        return(f'{ans}는 팰린드롬수입니다.')
    
    for j in range(int(len(text)/2)):
        if text[j]!=text[-1-j]:
            return(f'{ans}는 팰린드롬수가 아닙니다.')
        
        if j == int(len(text)/2)-1:
            return(f'{ans}는 팰린드롬수입니다.')
