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

# 전화번호 목록








def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
    

#### reduce 함수에 대해 정리 ####
## 앞선 계산에 누적해서 계산해줌
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# 10

reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 10)
## initializer에 10을 지정하면 10부터 시작
# 25

reduce(lambda x, y: x*y, range(1, 6))
# 120
