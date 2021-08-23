
# 기능 개발
## stack에다가 배포 일수를 쫙 넣어놓고서 이후에 조건문을 걸지 말고, 배포 일수를 계산하면서 조건문도 함께 걸어줄 것. 

import math

def solution(progresses, speeds):
    stack = []
    
    for p,s in zip(progresses, speeds):
        # stack이 비어있으면 맨 앞에 넣어주고 시작 (그래야 비교할 수가 생성됨)
        if len(stack) == 0:
            stack.append([math.ceil((100-p)/s),1])
            
        # 기존 stack에 있는 수랑 다음으로 들어올 수를 판단
        elif stack[-1][0] < math.ceil((100-p)/s):
            stack.append([math.ceil((100-p)/s),1])
        else:
            stack[-1][1] += 1
            
    return [s[1] for s in stack]
        
        
## 다른 풀이

# [[5], [10,1,1], [20,2]] 이런식으로 묶은 후 각 길이 return
import math 
def solution(progresses, speeds):
    stack = []
    
    for p,s in zip(progresses, speeds):
        # stack이 비어있으면 맨 앞에 넣어주고 시작
        if len(stack) == 0:
            stack.append([math.ceil((100-p)/s)])
            
        # 기존 stack에 있는 수랑 다음으로 들어올 수를 판단
        elif stack[-1][0] < math.ceil((100-p)/s):
            stack.append([math.ceil((100-p)/s)])
        else:
            stack[-1].append(math.ceil((100-p)/s))
            
    return [len(s) for s in stack]
        	
	
	
## 다른 풀이 - pop() append() 활용 

# progresses = [93,30,5] / speeds = [1,30,5] / [7,3,9]

def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
	
# (progresses[0] + time*speeds[0]) >= 100 이 될때까지 time을 계속 늘려나감 (ex. time=7일때까지)
# 100을 만족하면 pop(0), count 증가
# 해당 time값 (7) 으로 그 다음 요소도 만족하는지 판단
# 만족하면 계속 pop(0), count 계속 증가 (+1) 
# 해당 time값 (7) 으로는 더이상 100이 넘어가지 않으면 즉 만족 안하면,
# 지금까지 쌓아둔 count는 반환하고, count=0으로 초기화한 후 다시 첫번째 부터 반복
	
	
--------------------------------------------------------------------------------------------
	
# 프린트기 
## 내가 짠 코드 - 테스트 케이스는 맞는데 범용성에서 실패
## 다시 풀기

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








	
--------------------------------------------------------------------------------------------
# 다리를 지나는 트럭
## 다시 풀기










	
--------------------------------------------------------------------------------------------



# 주식 가격
def solution(prices):
	answer = [0]*len(prices)
	for i in range(len(prices)):
		for j in range(i+1, len(prices)):
			if prices[i] <= prices[j]:
				answer[i] += 1
			else:
				answer[i] += 1
				break
	return answer








#################################### while True: 문 완벽 이해하기 ###########################################################


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

	


#################################### queue / deque 완벽 이해하기 ##########################################################

# queue는 선입선출 (데이터를 추가한 순서대로 제거)

queue = [4, 5, 6]
queue.append(7)
>>> queue : [4,5,6,7]

queue.pop[0]
>>> 4
>>> queue : [5,6,7]
	
queue.pop[0]
>>> 5
>>> queue: [6,7]
	

# collections.deque는 데이터를 양방향에서 추가, 제거 가능
from collections import deque

queue = deque([4, 5, 6])
queue.append(7)
queue.append(8)

queue
>>> deque([4, 5, 6, 7, 8])

queue.popleft()
>>> 4
queue.popleft()
>>> 5

queue
>>> deque([6, 7, 8])

# appendleft(x)는 데이터를 맨 앞에서 삽입
queue = deque([4, 5, 6])
queue.appendleft(3)
queue.appendleft(2)

queue
>>> deque([2, 3, 4, 5, 6])



#################################### defaultdict 완벽 이해하기 ##########################################################

# 문자열에 나타난 알파벳 횟수 계산
## 딕셔너리에 키가 있는지 확인 하고, 없으면 키를 만들어주고 초기값을 0으로 세팅해줌
fraom collections import difaultdict

letters = 'dongdongfather'
letters_dict = defaultdict(int)

for k in letters:
	letters_dict[k] += 1
	
letters_dict
>>> defaultdict(<class:'int'>, {'d':2, 'o':2, 'n':2, 'g':2, 'f':1, 'a':1, 't':1, 'h':1, 'e':1, 'r':1})


# list에서 여러개의 값을 합쳐야 한 때 
## 성과 이름 튜플에서 각 성에 대한 이름들을 합치는 문제

name_list = [('kim','sungsu'), ('kang','hodong'), ('park','jisung'), ('kim','yuna'), ('park','chanho'), ('kang','hodong')]
ndict = defaultdict(list)

for k,v in name_list:
    ndict[k].append(v)]

ndict
>>> defaultdict(list,
            {'kang': ['hodong', 'hodong'],
             'kim': ['sungsu', 'yuna'],
             'park': ['jisung', 'chanho']})


## hodong이 2번 중복 --> 초기값을 set으로 지정

name_list = [('kim','sungsu'), ('kang','hodong'), ('park','jisung'), ('kim','yuna'), ('park','chanho'), ('kang','hodong')]
nset = defaultdict(set)

for k,v in name_list:
    nset[k].add(v)     # list는 append로, set은 add로 요소 추가


>>> nset
defaultdict(set,
            {'kang': {'hodong'},
             'kim': {'sungsu', 'yuna'},
             'park': {'chanho', 'jisung'}})

