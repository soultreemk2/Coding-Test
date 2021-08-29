
##################### reduce 함수에 대해 정리  #####################
## 앞선 계산에 누적해서 계산해줌
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# 10

reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 10)
## initializer에 10을 지정하면 10부터 시작
# 25

reduce(lambda x, y: x*y, range(1, 6))
# 120



###################### 문자열 list를 sort할 경우 ######################

aa = ["12","56","123","567","1235"]

sorted_aa = sorted(aa)
sorted_aa
>>> ['12', '123', '1235', '56', '567']




########### defaultdict는 개수 셀때 말고 리스트 요소 묶을 때 쓸것 (vs collections.Counter) ###########
# 갯수 세는 거는 collections.Counter 쓰기

letters = 'dongdongfather'

letters_dict = defaultdict(int)
for k in letters:
    letters_dict[k] +=1
  
>> letters_dict

## 이것 보다는 
collections.Counter(letters)


## 다만 리스트(튜플)의 key별로 value를 묶고 싶을때는
# (성,이름) 에서 성별로 이름을 묶을 때

name_list = [('kim','sungsu'), ('kang','hodong'), ('park','jisung'), ('kim','yuna'), ('park','chanho'), ('kang','hodong')]
ndict = defaultdict(list)

for k,v in name_list:
    ndict[k].append(v)
  
>> ndict
>> defaultdict(list,
            {'kang': ['hodong', 'hodong'],
             'kim': ['sungsu', 'yuna'],
             'park': ['jisung', 'chanho']})


# 이때 중복 이름이 두 번 다 나옴 --> default를 set으로 설정
nset = defaultdict(set)

for k,v in name_list:
    nset[k].add(v) # set함수는 append가 아니라 add
  
>> nset
>> defaultdict(set,
            {'kang': {'hodong'},
             'kim': {'sungsu', 'yuna'},
             'park': {'chanho', 'jisung'}})



#################################### while True: 문 완벽 이해하기 ####################################################


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


