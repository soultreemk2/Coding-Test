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


---------------------------------------------------------------------------------------------

# 백준 - 전투

# 색깔 별로(W,B) 인접해 있는 병사들의 숫자를 구하기 (bfs)
# 색깔을 매개변수로 넣어서 해당 색깔에 대한 bfs만 계산하도록 구현

from collections import deque

visited = [[0] * n for i in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs_color(x,y,color):
    cnt = 0
    queue = deque()
    queue.append((x,y)) # bfs로 탐색된 좌표
    visited[x][y] = 1
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4): # 상하좌우로 탐색
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == color and visited[nx][ny] != 1:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    cnt += 1
    return cnt + 1


graph = [list(input()) for _ in range(5)]

white, blue = 0,0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and not visited[i][j]:
            white += bfs_color(i,j,'W') ** 2
        elif graph[i][j] == 'B' and not visited[i][j]:
            blue += bfs_color(i,j, 'B') ** 2
            
print(white,blue)

---------------------------------------------------------------------------------------------

# 백준 - 음식물 피하기

N = 3
M = 5
K = 5


trash = [[0]*M for i in range(N)]
visited = [[False]*M for i in range(N)]

for i in range(M):
    r, c = map(int, input().split())
    trash[r-1][c-1] = 1
    
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,1,-1]
queue = deque()

def dfs(x,y, trash):
    queue.append((x,y))
    cnt = 1
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<M:
                 if trash[nx][ny] == 1 and not visited[nx][ny]:
                        queue.append((nx,ny))
                        trash[nx][ny] = 2
                        visited[nx][ny] = True
                        cnt += 1
                        
        return cnt
                            
    

answer = 0
for i in range(N):
    for j in range(M):
        if trash[i][j] == 1 and not visited[i][j]:
            ans  = dfs(i,j, trash)
            answer = max(ans, answer)


---------------------------------------------------------------------------------------------

# 백준 - 음식물 피하기

