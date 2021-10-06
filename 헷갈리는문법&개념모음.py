
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

	

#################################### queue / deque(데크) 완벽 이해하기 ##########################################################

# queue는 선입선출 (데이터를 추가한 순서대로 제거)

queue = [4, 5, 6]
queue.append(7)
>>> queue : [4,5,6,7]

queue.pop[0] # 대괄호임
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




#################################### 힙(heap) 완벽 이해 ###########################################
# 힙은 정렬되지 않은 리스트에서 최소 값을 먼저 추출해주는 구조

# 정렬되지 않은 배열에서 k번째로 큰 요소 추출
import heapq

nums = [4,1,7,3,8,5] 
k = 3

heap = list()

# 1차 힙정렬
for n in nums:
    heapq.heappush(heap, n) # [1,3,5,4,8,7]

# (최소값 추출 -> 힙정렬 -> 최소값 추출) - k번 반복
for _ in range(k): # k번 추출
    heapq.heappop(heap)   

# [1,3,5,4,8,7] -> [3,5,4,8,7]           1번째 작은값 추출
# [3,5,4,8,7] -> [5,4,8,7] -> [4,5,8,7]  2번째 작은 값 추출
# [4,5,8,7]   -> [5,8,7]  ->  [5,7,8]    3번째 작은 값 추출

print(heapq.heappop(nums))
>> 5  # 3번째로 큰 값

---------------------------------------------------------------------------------------------------------
## heapiy 이용
heapq.heapify(nums)

for _ in range(len(nums)-k):
    heapq.heappop(nums)
    
print(heapq.heappop(nums))
>>> 5

---------------------------------------------------------------------------------------------------------
## 최대 힙
# 힙에 튜플(tuple)를 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

print(heap)
>>> [(-8, 8), (-7, 7), (-5, 5), (-1, 1), (-3, 3), (-4, 4)]

while heap:
  print(heapq.heappop(heap)[1])  # 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값을 취하면 됨 (우선순위에는 관심 x)

print(heap)
>>> 8 7 5 1 3 4



############################# list, map 함수 #####################################

# map은 리스트의 요소를 지정된 함수로 처리
## 리스트의 모든 실수를 정수로 변환하려면
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
  a[i] = int(a[i])

# map함수를 쓰면
a = list(map(int, a))
  
# 0~9까지의 숫자를 문자열로 변환
a = list(map(str, range(10)))
>>> a : ['0','1','2', ........ , '9']
  
  
  
######################### sorted 함수의 key 옵션 ######################################
 
# 제곱 수가 가장 작은 순서대로 sorting    
a = [ -1, -8, 3, -4, 2, 5, -7]
sorted(a, key=lambda x : x*x, reverse=False) 
print(a)
>>> [-1,2,3,-4,5,-7,8]  

# 튜플 정렬
a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]

c = sorted(a, key = lambda x : x[0]) 
>>> c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

d = sorted(a, key = lambda x : x[1]) 
>>> d = [(3, 0), (5, 1), (0, 1), (1, 2), (5, 2)]

  

################################ 두 리스트 간 중복 요소 추출/제거 ##############################
a = [1,2,3]
b = [2,3,5,6]

# 중복되지 않은 요소만 추출
a2 = [i for i in a if i not in b]
b2 = [j for j in b if j not in a]
>> a2: [1],  b2: [5,6]
		
# 중복된 요소만 추출
a2 = [i for i in a if i in b]
b2 = [j for j in b if j in a]
>> a2: [2,3],  b2: [2,3]
		

## set을 써도 나오나, 단점: set함수가 중복 요소를 제거함
a2 = list(set(a) - set(b))
b2 = list(set(b) - set(a))

# name에서 'A'만 제거 하고 싶을 경우,
name = "ADBDC"

list(set(name) - set(['A']))          # ['D','B','C'] 만 출력

[i for i in name if i not in ['A']]   # ['D','B','D','C'] 출력


############################ 두개의 중첩리스트 간 중복 요소 추출/제거 ##############################


코테에 나왔었음.. 추가하기












######################### 커스텀 정렬 (cmp to key) ######################################












########################## 소수 판별 알고리즘 ##########################
# 소수란 '1과 자기자신'을 제외한 숫자로 나누어지지 않는 수

def is_prime_number(x):
    if x == 1:
        return False
    else:
        for i in range(2, x): # 2부터 (x - 1)까지의 모든 수를 확인하며
            if x % i == 0:    # x가 해당 수로 나누어떨어진다면
                return False # 소수가 아님
        
    return True # for문에서 if문에 걸러지는게 아무것도 없으면, 즉 1과 자신을 제외한 수로는 나누어지지 않으면 소수임



############### permutation, combination ##########################

from itertools import permutations

a = [1,2,3]
permute = permutations(a,2)

print(list(permute))
>>> [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]


a = [1,2,3]
combi = combinations(a,2)
    
print(list(combi))
>>> [(1,2),(1,3),(2,3)]

## 만일 이거를 ['12','13','23'] 이렇게 표현하고 싶으면
arr = []
for p in list(permutations(a,2)):
    arr.append(''.join(list(map(str,p))))



#################### 문자열  ##########################
# 문자열 나누기
str = "Hi my name is limcoing" 
splitted_str = str.split() 
print(splitted_str)
>>> ['Hi', 'my', 'name', 'is', 'limcoing'] 

# 문자열 합치기
joined_str = ''.join(splitted_str) 
print(joined_str)
>>> Himynameislimcoing


a = ('1','2','5')
a_join = ''.join(a)
print(a_join)
>>> 125





