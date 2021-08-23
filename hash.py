# 완주하지 못한 선수

## aa에서 bb를 빼고자 할때 (뻬고 남는건 무조건 하나임)
aa = ['a','e','b','e']
bb = ['b','e','a']
>> ['e']


@ list(set(aa) - set(bb)) 
@ [i for i in aa if i not in bb]
 --> aa의 중복 요소를 무시해버림

    
# 풀이1
import collections
list(collections.Counter(aa) - collections.Counter(bb))
>>> ['b','a']


# 풀이2 - hash함수 이용: 남아있는 선수가 한명 이라는 가정이 성립할때만 가능
temp = 0
dic = {}

for a in aa:
    dic[hash(a)] = a
    temp += int(hash(a))
for b in bb:
    temp -= int(hash(b))

dic[temp]
>> ['b']


# 풀이3
def solution(aa, bb):
    aa.sort()  # ['a','b','e','e']
    bb.sort()  # ['a','b','e']
    for a,b in zip(aa,bb):
        if a != b:
            return a
        
    return aa[-1]  # ['a','b','e','c'] / ['a','b','e'] 처럼 for문을 다 돌았는데도 못찾은 경우는 마지막 요소가 정답임


def solution(aa, bb):
    aa.sort()
    bb.sort()
    for i in range(len(bb)):
        if aa[i] != bb[i]:
            return aa[i]
        
    return aa[-1]



-----------------------------------------------------------------------------------------------------------------
## 이 경우 ['b','b','e']를 뽑고싶으면?

aa = ['b','b','e','b','e']
bb = ['b','e']

temp = []
for i in list(lst.keys()):
    temp.append([i]*lst[i])
>> [['b', 'b'], ['e']]


-----------------------------------------------------------------------------------------------------------------
# 전화번호 목록

def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

   
## 해시를 이용한 정석 풀이
# 다시 풀기
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer



-----------------------------------------------------------------------------------------------------------------
# 위장
import collections
from functools import reduce

def solution(clothes):
    # 종류별로 옷의 개수
    cnt = collections.Counter([kind for name, kind in clothes])
    # 각 옷 종류별로 (안입은것, 1번째 옷, 2번째 옷, ... n번째 옷) 따라서 (옷 종류 개수)*(옷 개수+1) --> 아무것도 안입는 경우 - 1
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


## reduce 함수 대신

def solution(clothes):
    # 종류별로 옷의 개수
    cnt = collections.Counter([kind for name, kind in clothes])
    
    answer = 1
    for i in list(cnt.values()):
        answer *= (i+1)
        
    return answer - 1   
   
## defaultdict로 해시테이블 만들기 (collections.Counter대신)
cnt = collections.defaultdict(int)
for name, kind in clothes:
  cnt[kind] += 1
   
   
   
-----------------------------------------------------------------------------------------------------------------
### 파알인 11장 해시테이블(279p~) ###

# 보석과 돌
def solution(J,S):
 freqs = collections.Counter(S):
 answer = 0
 for j in J:
  if j in list(freqs.keys()):  # 이부분 생략 가능
   answer += freqs[j]

-----------------------------------------------------------------------------------------------------------------   
# 중복 문자 없는 가장 긴 부분 문자열
## 투 포인터 - 다시 

## 중복문자가 나타나면 거기서부터 start위치 재조정 --> 길이 다시 계산

def solution(s):
 used  = {}
 max_length = start = 0
 
 for index, char in enumerate(s):
  # 이미 등장한 문자면 start위치 조정
  if char in used and start <= used[char]:
   start = used[char] + 1
  # 길이 다시 계산
  else:
   max_length = max(max_length, index - start + 1)
  
  # 현재 위치도 항상 업데이트 --> 길이 측정 위해서
  used[char] = index
  
 return max_length


-----------------------------------------------------------------------------------------------------------------
# 상위 k빈도 요소
nums = [1,1,1,2,2,3]
k = 2
 
freqs = collections.Counter(nums)
heap = []

for f in freqs: # f는 key를 의미 (1,2,3)
    heapq.heappush(heap, (-freqs[f], f))  

topk = []
for _ in range(k):
    topk.append(heapq.heappop(heap)[1])
    
# value의 가장 큰 값 k개를 추출할 것이므로
# freqs[f] : value를 음수로 변환해서 넣기 (최소힙이므로) 
# heap에서 총 k번 추출하면 됨. 이때 얻고싶은 것이 key이므로 [1]


## 다른 풀이
# value가 k 이상인것만 추출
freq_lst = collections.Counter(nums).most_common(k) 

answer = []
for k, v in freq_lst:
    answer.append(k) 
 


    

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




########### defaultdict는 개수 셀때 말고 리스트 요소 묶을 때 쓸것 ###########
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
