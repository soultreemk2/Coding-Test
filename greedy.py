#### 파알인 문제 ####

# 배낭 문제
cargo = [
    (4,12),
    (2,1),
    (10,4),
    (1,1),
    (2,2)
]

def knapsack(cargo):
    capacity = 15
    pack = []

    # 단가가 높은 순대로 나열
    for c in cargo:
        pack.append((c[0]/c[1],c[0],c[1]))
        pack.sort(reverse=True)

    # 단가 순 그리디 계산
    total_value: float = 0    
        
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            total_value += p[1]*fraction
            break

    return total_value

----------------------------------------------------------------------------------

# 주식 팔고사기 좋은 시점 2
def stock2(stock):
    profit = []
    for i in range(len(stock)-1):
        if stock[i] < stock[i+1]:
            profit.append(stock[i+1] - stock[i])
    return sum(profit)
  
## 다른 풀이
# 매번 이익 계산해 0보다 크면 무조건 합산
def stock3(stock):
  return sum(max(stock[i+1] - stock[i], 0) for i in range(len(stock)-1))

----------------------------------------------------------------------------------

# 키에 따른 대기열 재구성
## 이해 못함. 다시 풀기
  

  
  
  
  
----------------------------------------------------------------------------------
# 태스크 스케줄러
## 이해 못함. 다시 풀기

def scheduler(tasks):
    counter = collections.Counter(tasks)
    result = 0

    while True:
        sub_count = 0

        for task, _ in counter.most_common(n+1):
            sub_count += 1
            result += 1

            counter.subtract(task)
            # 0 이하 아이템을 목록에서 완전히 제거
            counter += collections.Counter()

        if not counter:
            break
        
        result += n - sub_count + 1
        
    return result



  
----------------------------------------------------------------------------------
# 쿠키 부여

def coockies(g, s):
    g.sort()
    s.sort()
    
    i = j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]: # 크기 만족 --> 다음 아이 판단을 위해 i+1
            i += 1       # 만족한 아이 수 count
        j += 1           # 쿠키도 다음 쿠키로 j+1
                         ## 만일 아이가 크기만족 못하면(if문 만족x) --> 아이는 그대로 두고 쿠키만 그 다음 쿠키로 재판단
    return i




#### 프로그래머스 문제 ####

# 체육복
## 틀린 코드 - 정확도 50%
def solution(n, lost, reserve):
    reserve_2 = [r for r in reserve if r not in lost]
    lost_2 = [l for l in lost if l not in reserve]
    reserve_2.sort()
    lost_2.sort()
    
    i = j = 0
    while i < len(lost_2) and j < len(reserve_2):
        if lost_2[i] == reserve_2[j]+1 or lost_2[i] == reserve_2[j]-1:
            i += 1
        j += 1
            
    return n - len(lost_2) + i


## 정답 코드

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    
    for r in _reserve:
        if r-1 in _lost:
            _lost.remove(r-1)
        elif r+1 in _lost:
            _lost.remove(r+1)
            
    return n - len(_lost)

----------------------------------------------------------------------------------

# 조이스틱 

















######################## 두 리스트 간 중복 요소 추출/제거 #####################
a = [1,2,3]
b = [2,3,5,6]

# 중복되지 않은 요소만 추출
a2 = [i for i in a if i not in b]
b2 = [j for j in b if j not in a]
>> a2: [1],  b2: [5,6]

## 동일 코드
a2 = list(set(a) - set(b))
b2 = list(set(b) - set(a))


# 중복된 요소만 추출
a2 = [i for i in a if i in b]
b2 = [j for j in b if j in a]
>> a2: [2,3],  b2: [2,3]













