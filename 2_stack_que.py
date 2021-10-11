
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
	
	
------------------------------------------------------------------------------------------------------------------------------------------
# 프린트기 

# que에다가 queue에 있는 요소를 내림차순으로 정렬해서 append 한 뒤 location을 찾는 방식
# queue.pop(0)가 나머지 요소의 최대값보다 작으면 queue뒤에 append
# 나머지 요소의 최대값보다 크면 que에 새롭게 append
# 해당 작업을 queue에 있는 모든 요소들에 반복 (즉, que길이가 priority길이와 같을때까지)

## 이 코드의 문제점
# max함수를 쓰면 queue의 마지막 요소가 pop되었을 때 비교할 요소가 없음
# 따라서 queue의 마지막 요소는 pop한 후 비교 없이 바로 que에 append (len(que) == len(priorities) - 1)
# 하지만 일부 케이스에서 time-out

from collections import deque

def solution(priorities,location):
    que = []
    queue = [(i,p) for i,p in enumerate(priorities)]
    priority = [(i,p) for i,p in enumerate(priorities)]
    
    while True:
        cur = queue.pop(0)
        if cur[1] < max(q[1] for q in queue):
            queue.append(cur)
        else:
            que.append(cur)
            if len(que) == len(priorities) - 1:
                que.append(cur)
                return(que.index(priority[location]) + 1)
                break


# any를 쓰면 문제 해결 - any는 빈 리스트와도 비교가 가능 (무조건false로 나옴)
def solution(priorities,location):
    que = []
    queue = [(i,p) for i,p in enumerate(priorities)]
    priority = [(i,p) for i,p in enumerate(priorities)]
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            que.append(cur)
            if len(que) == len(priorities):   # 해당 조건을 만족할때까지 while문 반복
                return que.index(priority[location]) + 1
                break

	
------------------------------------------------------------------------------------------------------------------------------------------
# 다리를 지나는 트럭
## 코드 구조를 익혀두기 !!!!

def solution(bridge_length, weight, truck_weights):
    ing = [0] * bridge_length
    time = 0
    wait = truck_weights
    
    while ing:
        a = ing.pop(0)
        time += 1
        if wait:
            if sum(ing) + wait[0] <= weight:
                ing.append(wait[0])
                wait.pop(0)
            else:
                ing.append(0)
                
    return time


# 예시
wait = [7,2,4,5,6]
ing = [0,0,0]
weight = 12

time = 0
while ing:  # ing리스트가 빌때까지 다음 코드를 반복
    a = ing.pop(0)
    time += 1
	
    if wait: # 이 조건문을 걸어주지 않으면, wait요소가 다 빠져나갔을 때 wait.pop(0)가 실행X 
             # 따라서 wait에 요소가 남을때까지만 조건문을 실행해주고, ing에 남아있는 요소들은 if문 밖 while문에서 처리 
        if sum(ing) + wait[0] <= weight:
            ing.append(wait[0])
            wait.pop(0)
        else:
            ing.append(0)
            
    print(ing, wait)

>>>
[0, 0, 7] [2, 4, 5, 6]
[0, 7, 2] [4, 5, 6]
[7, 2, 0] [4, 5, 6]
[2, 0, 4] [5, 6]
[0, 4, 5] [6]
[4, 5, 0] [6]
[5, 0, 6] []
[0, 6] []
[6] []
[] []

## 즉 [5,0,6] [] 이 되었을때 if wait문을 걸어줌으로써 sum(ing)~ 이하 구문이 실행되지 않고 while문 내의 ing.pop(0)만 계속 실행됨 (ing가 빌때까지)

------------------------------------------------------------------------------------------------------------------------------------------

# 주식 가격

## 풀이1

def solution(prices):
    answer = [0]*len(prices) 
    
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:         # [i] > [j] 인 구간을 만나면
                answer[i] += 1
                break    # j를 더이상 움직이지 않음, 그 다음 i로 넘어가기
                
    return answer


## for i / for j 대신 while문 써도 가능

def solution(prices):
    answer = [0]*len(prices)    
    
    i = -1
    while i < len(prices):
        i += 1
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
                
    return answer



## 풀이2
# deque로 풀기


def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:  # prices 를 모두 탐색해서 [] 되면 stop
        c = prices.popleft()
	
        count = 0
#         for i in prices: # 나머지 숫자 하나씩 다 살펴보기
#             if c > i:
#                 count += 1
#                 break	
#            count += 1    # 계속 +1 누적하다가 if문(c>i)을 만나면 +1하고서 stop
	
        answer.append(count)
        
    return answer


## 이렇게 해도 됨

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:  # prices 를 모두 탐색해서 [] 되면 stop
        c = prices.popleft()
	
        count = 0
#         for i in prices: # 나머지 숫자 하나씩 다 살펴보기
#             if c <= i:
#                 count += 1
#             else:
#                 count += 1
#                 break
        answer.append(count)

    return answer


### 신기한점은 prices를 deque선언 안하고 그냥 stack으로 보고 prices.pop(0)로 하면 time-out임 -왜지?




------------------------------------------------------------------------------------------------------------------------------------------
# 파알인(245p~)
------------------------------------------------------------------------------------------------------------------------------------------

# 유효한 괄호

def solution(s):
    stack = []
    table = {
        ')':'(',
        '}':'{',
        ']':'[',
    }

    for char in s:
        if char not in table:  
            stack.append(char)            # ['(']
        elif table[char] != stack.pop():  
            return False
    return len(stack) == 0 # 예외처리 (스택이 비어있는지 여부)


------------------------------------------------------------------------------------------------------------------------------------------

# 중복문자 제거

s = "cbacdcbc"

def solution(s):
	stack = []
	counter = collections.Counter(s)
	
	for char in s:
	    counter[char] -= 1 # 체크한것 (for문 돈것은 count 하나씩 차감)

	    if char in stack:  # char가 이미 stack에 들어가있으면 검사할 필요x, 스킵(다음 char로 continue)
		continue

	    while stack and char < stack[-1] and counter[stack[-1]] > 0:
		stack.pop()

	    stack.append(char) # if문 걸릴게 없으면 (stack이 비어있으면) 얘부터 실행

	return ''.join(stack)



------------------------------------------------------------------------------------------------------------------------------------------

# 일일온도
## 다시 풀기 - 어렵..

def dailyTemperatures(T):
	answer = [0] * len(T)
	stack = []

	for i, temp in enumerate(T):
	    while stack and T[stack[-1]] < temp:
		index = stack.pop()
		answer[index] = i - index
	    stack.append(i)
	
	return answer


------------------------------------------------------------------------------------------------------------------------------------------
# 백준 - 괄호의 값


s = input().rstrip()
stack = []
answer = 0

for i in s:
    if i == ")":
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == "(":
                if t == 0:
                    stack.append(2)
                else:
                    stack.append(2 * t)
                break
            elif top == "[":
                print(0)
                exit(0)
            else:
                t = t + int(top)
    elif i == "]":
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == "[":
                if t == 0:
                    stack.append(3)
                else:
                    stack.append(3 * t)
                break
            elif top == "(":
                print(0)
                exit(0)
            else:
                t = t + int(top)
    else:
        stack.append(i)

for i in stack:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        answer += i

print(answer)




