------------------------------------------------------------------------------------------------------------------------------------------
# 파알인(585p~)
------------------------------------------------------------------------------------------------------------------------------------------

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

    # 단가 가치가 높은 순대로 나열
    for c in cargo:
        pack.append((c[0]/c[1],c[0],c[1]))
        pack.sort(reverse=True)

    # 단가 순 그리디 계산
    total_value: float = 0    
    
    # 가치순대로 하나씩 짐을 싣고
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        # 정수까지는 다 싣고나서 남은 무게 만큼은 쪼개서 넣으면 됨
        else:
            fraction = capacity / p[2]
            total_value += p[1]*fraction
            break

    return total_value

-----------------------------------------------------------------------------------------------------------------

# 주식 팔고사기 좋은 시점 2
## 몇번이든 사고팔수 있으니까 greedy 하게 내리면 사고/오르면 팔고를 계속 반복
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

-----------------------------------------------------------------------------------------------------------------

# 키에 따른 대기열 재구성
## 키가 큰 순서대로 인덱스 위치에 넣어주기 (키 큰 애들을 먼저 배열해주고 작은 애들을 사이사이 넣어주어야 함)

[7,0]
[7,0] [7,1]                         # 1번째 인덱스에 [7,1]
[7,0] [6,1] [7,1]                   # 1번째 인덱스에 [6,1]
[5,0] [7,0] [6,1] [7,1]             # 0번째 인덱스에 [5,0]
[5,0] [7,0] [5,2] [6,1] [7,1]       # 2번째 인덱스에 [5,2]
[5,0] [7,0] [5,2] [6,1] [4,4] [7,1] # 4번째 인덱스에 [4,4]


import heapq

# 최대힙으로 구현해서 최대값부터 차례대로 추출(7,7,6,5,5,4)해서 해당 인덱스에 append
def solution(people):
    heap = []
    for p in people:
        heapq.heappush(heap,(-p[0],p[1])) # 최대힙 구현

    answer = []
    for _ in range(len(heap)): # 차례대로 추출, 해당 인덱스에 삽이
        a = heapq.heappop(heap)
        answer.insert(a[1], [-a[0],a[1]]) # inset(위치, 삽입요소)
        
    return answer

  
  
-----------------------------------------------------------------------------------------------------------------
# 태스크 스케줄러
## 이해 못함. 다시 풀기 - 이건 좀 어렵....

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



-----------------------------------------------------------------------------------------------------------------
# 주유소

# 풀이1 - O(N^2)

# 모든 주유소를 방문 가능한지 점검하고 가능한 경우 해당 출발점을 return
# 중간에 끊길 경우 (fuel가 음수) 다음번 출발점으로 넘어가서 다시 반복

# start = 0일때 --> 0,1,2,3,4 순차방문 --> 중간에 끊기면(연료<0되는지점발생) 다음 출발점으로
# start = 1일때 --> 1,2,3,4,0 순차방문 --> 중간에 끊기면(연료<0되는지점발생) 다음 출발점으로
# start = 2일때 --> 2,3,4,0,1 순차방문 --> 

## 안끊기고 쭉 for문이 돌아가면 해당 start값을 return


def solution(gas,cost):
    fuel = 0
    for start in range(len(gas)):
        for i in range(start, len(gas)+start):
            index = i % len(gas)

            can_travel = True
            if fuel + gas[index] - cost[index] < 0: # 출발지점에서 중간에 끊기면(연료<0) for문 break. 다음 start로
                can_travel = False 
                break
            else:
                fuel += gas[index] - cost[index]  # start 이후 한번도 안끊겼다면 can_travel = True

        if can_travel:
            return start
        
    return -1



# 풀이2 - O(N)

# 성립되지 않는 지점(연료<0)이 있다면 그 앞은 전부 출발점이 될 수 없음
# 해당 지점을 제외하면서 출발점을 찾기

def solution(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    
    start, fuel = 0,0
    for i in range(len(gas)):
        # 출발점이 안되는 지점 판별
        if fuel + gas[i] - cost[i] < 0:
            start = i+1  # 출발점이 안되는 지점은 제외하고 그 다음 지점을 시작점으로
            fuel = 0 
        else:
            fuel += gas[i] - cost[i]




  
-----------------------------------------------------------------------------------------------------------------
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




------------------------------------------------------------------------------------------------------------------------------------------
# 프로그래머스
------------------------------------------------------------------------------------------------------------------------------------------

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

-----------------------------------------------------------------------------------------------------------------

# 조이스틱 - 다시 풀기
## 틀린 코드 - A가 연달아 나오는 경우를 고려 못함
def solution(name):
    dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,
           'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
           'O':13,'P':12,'Q':11,'R':10,'S':9,'T':8,'U':7,
           'V':6,'W':5,'X':4,'Y':3,'Z':2}
    
    abc = []
    name2 = [i for i in name if i not in ['A']]
    
    for i in range(len(name2)):
        abc.append(dic[name2[i]] - 1)

    if 'A' in name:
        if (name[1] == 'A' or name[0] == 'A') and name[-1] == 'A':
            move = len(name) - 3 
        elif name[1] == 'A' or name[0] == 'A':
            move = len(name) - 2
    else:
        move = len(name) - 1
        
    return sum(abc) + move


# 정답코드1
def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min(min_move, i + i + len(name) - next)
    answer += min_move
    return answer


#정답코드2

def solution(name):
    change = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    idx, answer = 0, 0

    while True:
        answer += change[idx]
        change[idx] = 0

        if sum(change) == 0:
            break

        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1

        while change[idx + right] == 0:
            right += 1

        answer += left if left < right else right
        idx += -left if left < right else right
        
    return answer


-----------------------------------------------------------------------------------------------------------------
# 큰 수 만들기
        
# 정답 풀이
## [4,1,7,7,2] 이런 경우 4,1 모두 7보다 작으니까 둘 다 지우고 나서 7을 append해야함 --> while stack 조건문을 추가 
## if문만 쓰면 1 하나만 지우고 4는 그대로 두게 됨
              
def solution(number, k):
    # stack에 입력값을 순서대로 삽입 
    stack = [number[0]]
    for num in number[1:]:
        # 들어오는 값이 stack 값보다 크면, 기존의 값을 제거하고 새로운 값으로 바꿈 
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)  # while문이 안걸리면 무조건 append
              
    # 만일 충분히 제거하지 못했으면 남은 부분은 단순하게 삭제
    # 이렇게 해도 되는 이유는 이미 큰 수부터 앞에서 채워넣었기 때문 
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


-----------------------------------------------------------------------------------------------------------------
# 구명보트
## 가장 효율적으로 태우려면, 무게가 가장 작은 사람과 가장 큰사람을 엮어줘야함   
    
## 투 포인터
def solution(people, limit):
    people.sort()
    temp = []
    a = 0
    b = len(people) - 1
    
    while a < b:
        if people[a] + people[b] <= limit:
            a += 1
            temp.append(people[a])
            temp.append(people[b])
        b -= 1
        
    return len(people) - len(temp) + len(temp)//2
  
              
def solution(people, limit):
    answer = 0
    
    people.sort()
    a = 0
    b = len(people) - 1
    
    while a < b:
        if people[a] + people[b] <= limit:
            a += 1
            answer += 1
        b -= 1
        
    # 보트 수 + 남은 인원
    return answer + (len(people) - 2*answer)
    
         
## stack으로도 풀 수 있음
## 엮어지면 --> 둘다 pop / 안엮어지면 --> 가장 큰 사람을 따로 태우고 (+1) 그보다 바로 앞 무게 사람을 엮어봄  
 
def solution(people, limit):
    answer = 0
    poo = sorted(people)
    while poo:
        if len(poo) == 1: # 예외처리
            answer += 1
            break
        if poo[0] + poo[-1] > limit:
            poo.pop()
            answer += 1
        else:
            poo.pop(0)
            poo.pop()
            answer += 1
    return answer              


