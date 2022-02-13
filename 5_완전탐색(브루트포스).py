## 완전탐색은 간단히 가능한 모든 경우의 수를 다 체크해서 정답을 찾는 방법 (브루트 포스)
# ① Brute Force 기법 - 반복 / 조건문을 활용해 모두 테스트하는 방법
# ② 순열(Permutation) - n개의 원소 중 r개의 원소를 중복 허용 없이 나열하는 방법
# ③ 재귀 호출
# ④ 비트마스크 - 2진수 표현 기법을 활용하는 방법
# ⑤ BFS, DFS를 활용하는 방법



# 모의고사

def solution(answer):
    result = []
    p_1 = list(range(1,6))
    p_2 = [2,1,2,3,2,4,2,5]
    p_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c_1, c_2, c_3 = 0, 0, 0
    
    for i in range(len(answer)):
        if answer[i] == p_1[i%len(p_1)]:
            c_1 += 1
        if answer[i] == p_2[i%len(p_2)]:
            c_2 += 1
        if answer[i] == p_3[i%len(p_3)]:
            c_3 += 1
            
    for i,j in enumerate([c_1,c_2,c_3]):
        if j == max([c_1,c_2,c_3]):
            result.append(i+1)
        
    return result

---------------------------------------------------------------------------------------------------------

# 소수 찾기
from itertools import permutations

def solution(numbers):
    # 소수 판별함수
    def is_prime_number(x):
        if x == 1:
            return False
        else:
            for i in range(2, x):
                if x % i == 0:   # 자기자신보다 작은 모든 수로 나눌때
                    return False # 나누어떨어지는게 하나라도 존재하면 소수가 아님(false)
        return True 
    
    per_list = []
    per_list_final = []
    for i in range(len(numbers)):
        for p in list(permutations(numbers,i+1)):
            per_list.append(''.join(list(map(str,p))))
            per_list_final = list(set(per_list))
    # permutation으로 numbers에서 만들수 있는 모든 숫자의 조합을 append
    ## set으로 중복요소 제거
    
    temp = []
    for i in per_list_final:
        if i.startswith('0'):
            temp.append(i)
            per_list_final = list(set(per_list_final) - set(temp))
    # 예외처리 - 이때 맨 앞에 0이 오는 숫자는 리스트에서 제거
    
    answer = 0
    for num in per_list_final:
        if is_prime_number(int(num)):
            answer += 1

    return answer
    # 해당 리스트에서 소수인 것들의 갯수만 count
    
  
---------------------------------------------------------------------------------------------------------

# 카펫

def solution(brown, yellow):
    x_list = []
    y_list = []
    xy_list = []
    result = []
    
    for y in range(1,yellow+1):
        if yellow % y == 0 and yellow // y >= y:
            x_list.append(yellow // y)
            y_list.append(y)

    for i in range(len(x_list)):
        xy_list.append((x_list[i],y_list[i]))

    for xy in xy_list:
        if (xy[0] + xy[1])*2 + 4 == brown and xy[0]*xy[1] == yellow:
            return [xy[0]+2,xy[1]+2]


---------------------------------------------------------------------------------------------------------
## 백준 - 연산자 끼워넣기 (재귀함수)

# 브루트포스 풀이

from itertools import permutations

n = int(input())
o = ['+','-','*','/']
num = list(map(int,input().split()))
op = list(map(int,input().split())) # + - * /
oper = []
for i in range(4):
    for j in range(op[i]):
        oper.append(o[i])
        
operator = list(set(permutations(oper, len(oper)))) ## (+,+..)처럼 중복된 문자로 인해 perm결과도 중복된것 많음 --> set으로 제거        

# 연산자 정의
answer = []
for op in operator:
    n = num[0]
    for i in range(len(num)-1):
        if op[i] == '+':
            n += num[i+1]
        elif op[i] == '-':
            n -= num[i+1]
        elif op[i] == '*':
            n *= num[i+1]
        else:
            if n//num[j+1] < 0:
                n = -(-n//num[i+1])
            else:
                n = n//num[i+1]
                
    answer.append(n)
print(max(answer))
print(min(answer))


## 재귀함수 풀이

n = 6
numbers = [1,2,3,4,5,6]
add, sub, mul, div = 2,1,1,1
 
 
answer = []

def solve(i, num, add, sub, mul, div):
    # 종료조건
    if i == n:
        answer.append(num)
        
    if add > 0:
        solve(i+1, num+numbers[i], add-1, sub, mul, div)
    if sub > 0:
        solve(i+1, num-numbers[i], add, sub-1, mul, div)
    if mul > 0:
        solve(i+1, num*numbers[i], add, sub, mul-1, div)
    if div > 0:
        if num < 0:
            solve(i+1, -(-num//numbers[i]), add, sub, mul, div-1)
        else:
            solve(i+1, num//numbers[i], add, sub, mul, div-1)
    
    
solve(1, numbers[0], add, sub, mul, div)

print(max(answer))
print(min(answer))



---------------------------------------------------------------------------------------------------------
## 백준 - 사탕게임

n = int(input())
candies=[]
ans = 1
 
for i in range(n):
    temp =[]
    temp_str = input()
    for j in range(n):
        temp.append(temp_str[j])
    candies.append(temp)
    

    
# 몇개 먹을 수 있는지 찾는 함수
def search():
    global ans
    # 같은 열에서 몇개의 중복 사탕이 존재하는지 (행 방향으로 탐색)
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candies[i][j]== candies[i][j+1]:
                cnt+=1
                ans = max(cnt,ans)
            else:
                cnt = 1
        #ans = max(cnt,ans)
    
    # 같은 행에서 몇개의 중복 사탕이 존재하는지 (열 방향으로 탐색)
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candies[j][i] == candies[j+1][i]:
                cnt+=1
                ans = max(cnt,ans)
            else:
                cnt = 1
        #ans = max(cnt,ans)
        
        
# [모든 인접한 두 자리 뒤집어보고 찾기]    
# 가로 뒤집기
for i in range(n):
    for j in range(n-1):
        candies[i][j],candies[i][j+1] = candies[i][j+1],candies[i][j]
        search()
        # 원복
        candies[i][j],candies[i][j+1] = candies[i][j+1],candies[i][j]

# 세로 뒤집기
for i in range(n):
    for j in range(n-1):
        candies[j][i],candies[j+1][i] = candies[j+1][i],candies[j][i]
        search()
        # 원복
        candies[j][i],candies[j+1][i] = candies[j+1][i],candies[j][i]

        
print(ans)




```
1) 투포인터 - 구간의 크기가 가변적
2) 슬라이딩윈도우 - 구간 크기가 고정
이전의 결과(w-1)를 써먹는 방향
매번 처리되는 중복 요소를 버리지 않고 재사용 -> 계산낭비없이 효율적으로 처리
```

# 백준 - 블로그
N, X = map(int, input().split())
data = list(map(int, input().split())

value = sum(data[:X])

if max(data) == 0:
    print("SAD")
    
else:
    max_value = value
    max_cnt = 1

    for i in range(X, N):
        value += data[i]
        value -= data[i-X]

        if value > max_value:
            max_value = value
            max_cnt = 1
    
        elif value=max_value:
            max_cnt += 1
            
print(max_value)
print(max_cnt)
            
----------------------------------------------------------------------------------------------------
 # 백준 - 게으른 백곰
            
            
