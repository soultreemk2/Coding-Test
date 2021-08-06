###### while True: 문 완벽 이해하기 ######


# 특정 input 값을 받기 전까지 계속해서 코드가 실행되게 하고 싶을 때 이용

while True:
	stop_value = int(input('1을 입력할 때까지 반복 됩니다.'))   # if조건문을 만족할때 까지 해당 문 계속 반복
    if stop_value == 1:
        break
        

# answer로 stop이 입력 될때까지 계속 반복 

while True:
    print('continue or stop? [continue/stop]:')
    answer = input()
    
    if answer == 'continue':
        print('>> continue again!')

    elif answer == 'stop':
        print('>> stop here!')
        break

    else:
        print('>> wrong answer!')

	
	
# 프린트기 
## 내가 짠 코드 - 테스트 케이스는 맞는데 범용성에서 실패

def solution(priorities, location):
    que = [(i,j) for i,j in enumerate(priorities)]
    queque = [(i,j) for i,j in enumerate(priorities)]

    while True:
        aa = que.pop(0)

        if aa[1] < max([que[i][1] for i in range(len(que))]):
            que.append(aa)
        else:
            que.insert(0,aa)
            break
        
    return(que.index(queque[location]) + 1)
