# 프로그래머스 - 타겟 넘버


answer = 0
def DFS(idx, numbers, target, value):
    global answer
    if idx == len(numbers) and target == value:
        answer += 1
        return
    if idx == len(numbers):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])

def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer


---------------------------------------------------------------------------------------------

# 파알인- 전화번호 문자 조합

digits = "235"
dic = {"2":"abc", "3":"def", "4":"ghi","5":"jkl",
       "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

result = []

def dfs(index, path):
    # 끝까지 탐색 후 백트래킹 (조건에 맞는 것만 결과에 append)
    if len(path) == len(digits):
        result.append(path)
        return

    for i in range(index, len(digits)):
        for j in dic[digits[i]]:
            dfs(i+1, path+j)
            
    return result
  
  
>>> dfs(0,"")  
  
  

---------------------------------------------------------------------------------------------


# 파알인- 조합의 합

result = []

def dfs(csum, index, path):
    # 종료조건
    if csum < 0:
        return
    if csum == 0:
        result.append(path)
        return
    
    for i in range(index, len(candidates)):
        dfs(csum - candidates[i], i, path + [candidates[i]])
        
    return result  

# candidates = [2,3,5]
# target = 8

>>> dfs(target, 0, [])
>>> [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


## 프로그래머스 형식에 맞추면

result = []

def dfs(candidates, csum, index, path):
    # 종료조건
    if csum < 0:
        return
    if csum == 0:
        result.append(path)
        return
    
    for i in range(index, len(candidates)):
        dfs(candidates, csum - candidates[i], i, path + [candidates[i]])
        
    return result  

def solution(candidates, target):
    answer = dfs(candidates, target,0,[])
    return answer


>>> solution([2,3,5],8)
>>> [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


---------------------------------------------------------------------------------------------

# 파알인- 부분 집합
result = []

def dfs(nums, index, path):
    result.append(path)
    
    for i in range(index, len(nums)):
        dfs(nums, i+1, path + [nums[i]])
        
    return result

def solution(nums):
    answer = dfs(nums, 0, [])
    return answer
  
  
>> solutions([1,2,3])
>>> [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]




---------------------------------------------------------------------------------------------

# 백준 - 미로탐색
## bfs를 이용한 최단경로 탐색

N, M = map(int, input().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input())))


def bfs(x,y):
    dx = [-1,1,0,0] # 좌/우
    dy = [0,0,1,-1] # 상/하
    
    queue = [(x,y)]
    
    # 상하좌우가 1인 것이 여러개 있을수 있으므로 while문이 끝날때까지 반복
    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위가 벗어나지 않는 애들만
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append((nx,ny))
                    
    return matrix[N-1][M-1]
    
    
print(bfs(0,0))












