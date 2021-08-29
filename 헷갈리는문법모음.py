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
from collections import difaultdict

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

