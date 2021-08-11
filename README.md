# Coding-Test
프로그래머스 코테


### DFS, BFS (깊이, 너비 우선탐색)
- 그래프 순회 문제에서 사용됨
- 그래프의 각 정점을 방문하는 문제
- 코테에서 대부분의 그래프 탐색은 DFS로 구현

1) DFS (깊이 우선 탐색)
- 스택/재귀로 구현


2) BFS (너비 우선 탐색)
- 큐로 구현 (그래프 최단 경로 구하는 문제에 사용)

# ![image](https://user-images.githubusercontent.com/50647833/129039103-9f6bb880-f74d-4d72-8fcc-65450ae70fc4.png)

그래프를 표현하는 방법 : 인접리스트 (출발노드를 key, 도착노드를 value로)
```
graph = { 
1: [2,3,4],
2: [5],
3: [5],
4: [],
5: [6,7],
6: [],
7: [3],
}
```

#### DFS로 그래프 탐색
1) 스택으로 구현
```
def iterative_dfs(start_v):
  discovered = []
  stack = [start_v]
  while stack:
    v = stack.pop()
    if v not in discovered:
      discovered.append(v)
      for w in graph[v]:
        stack.append(w)
        
  return discovered


## 변수명을 이해 쉽게 

def iterative_dfs(start):
    visit_record = []
    next_visit_list = [start]

    while next_visit_list:
        now_visit = next_visit_list.pop()

        if now_visit not in visit_record:
            visit_record.append(now_visit)

            for w in graph[now_visit]:
                next_visit_list.append(w)
                
    return visit_record
```

2) 재귀 구조로 구현
```
def recursive_dfs(v, discovered=[]):
  discovered.append(v)
  for w in graph[v]:
    if not w in discovered:
      discovered = recursive_dfs(w, discovered)
      
  return discovered
```


#### BFS로 그래프 탐색
1) 큐로 구현
```
def iterative_bfs(start_v):
  discovered = [start_v]
  queue = [start_v]
  
  while queue:
    v = queue.pop(0)
    for w in graph[v]:
      if w not in discovered:
        discovered.append(w)
        queue.append(w)
        
  return discovered
```

2) 재귀로 구현 불가. 명심!









