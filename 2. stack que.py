#code test

#스택 & 큐


## 1. 주식가격
### 1
def solution10(prices):
    answer=[0]*len(prices)
    for i in range(len(prices)-1):
        for v in range(i+1, len(prices)):
            answer[i]+=1
            if prices[i]>prices[v]:
                break
    return answer
        



### 2 스택큐 개념 사용
from collections import deque
def solution11(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer




### 3 이진명 (효율성 통과 x)
def solution12(prices):
    answer = list(range(len(prices)))
    answer.reverse()
    for i in range(len(prices)):
        per_min = min(prices[i:])
        if prices[i] != per_min:
            tmp = list(filter(lambda y: y < prices[i], prices[i:]))
            answer[i] = prices[i:].index(tmp[0])
    return answer









## 2. 기능 개발
### 1 마지막 테스트 케이스 계속 오류
def solution20(progresses, speeds):
    answer=[]
    b=[]
    #며칠걸리는지 계산해서 리스트(b)로 반환
    for i in range(len(progresses)):
        b.append((100-progresses[i])//speeds[i] if (100-progresses[i])%speeds[i] == 0 else (100-progresses[i])//speeds[i] + 1)
                
    #until the next largest number 로 2D리스트 만들기
    current = b[0]  #첫번째 기준(리스트의 첫번째 요소)
    temp = []       
    res = []
    for num in b:
        if num > current:
            res.append(temp)
            current = num       #기준을 계속 초기화 할 수 있다
            temp = []
        temp.append(num)        
    res.append(temp)
    
    #2D 리스트의 길이
    for i in res:
        answer.append(len(i))
    
    return answer

    

### 2 이진명코드 돌리지말자 악성코드를 심었다;
def solution(progresses, speeds):
    num = [0,]
    answer = []
    due_date = [0] * len(progresses)
    progresses = list(map(lambda x : 100-x, progresses))
    for i in range(len(progresses)):
        due_date[i] = progresses[i]//speeds[i] if progresses[i] % speeds[i] == 0 else progresses[i]//speeds[i] + 1
    for i in num:
        tmp = list(map(lambda x : 0 if x <= due_date[i] else 1, due_date[i:]))
        if 1 in tmp:
            answer.append(tmp[0:tmp.index(1)].count(0))
            num.append(tmp.index(1))
        else:
            answer.append(tmp.count(0))
    return answer
            








## 3. 다리를 지나는 트럭        
### 1 5번 테스트 시간초과
### sum() 은 O(N) 이여서, 매번 sum 을 계산해야하니 복잡해짐.
def solution(bridge_length, weight, truck_weights):
    ing=[]
    truck_weights.reverse()
    while True:
    #초반에 ing 리스트가 다리길이보다 짧을 때
        if len(ing) < bridge_length:
            if sum(ing)+truck_weights[-1] <= weight:
                ing.append(truck_weights.pop())
            else:
                ing.append(0)
    #ing 리스트가 다리길이 보다 길 때
        else:
            if sum(ing[-(bridge_length-1):])+truck_weights[-1] <= weight:
                ing.append(truck_weights.pop())
            else:
                ing.append(0)
        if len(truck_weights) == 0:
            break
    return len(ing)+bridge_length

    
    
bridge_length=2
weight=10
truck_weights=[7,4,5,6]
    








## 4. 프린터
### 1 문제 이해를 잘못함. max 하나만 앞에 두고 나머지 신경 안쓰는 줄
def solution40(priorities, location):
    a=priorities.index(max(priorities)) + 1     #max 의 위치 1 부터 
    location= location + 1                      #위치 1부터
    answer = (location + len(priorities) - (a - 1) )
    if answer > len(priorities):
        answer = answer - len(priorities)
    return answer




### 2
def solution(priorities, location):
    answer = 0

    array1 = [c for c in range(len(priorities))] # index 위치 저장 
    array2 = priorities.copy() # 값 저장 (출력되는 값)

    i = 0
    while True:
        if array2[i] < max(array2[i+1:]):
            array1.append(array1.pop(i))
            array2.append(array2.pop(i))
        else:
            i += 1

        if array2 == sorted(array2, reverse=True):
            break

    return array1.index(location) + 1




### 3
def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans
            
        
        
    
    
    
    
    
    
    

    
    
    
    