# 더 맵게
## (내가 짠거)

import heapq

def solution(scoville,K):
    solution = 0
    heapq.heapify(scoville)
        
    while len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        solution += 1
        heapq.heappush(scoville, a+2*b)

        if scoville[0] >= K:
            return solution
        
    # while문을 다 돌고 난 후에도 (즉 a,b를 heap에 계속 넣어주는 작업을 scoville에 원소가 남아있을 때 까지 무한 반복) 했음에도
    # 첫번째 요소가 k보다 값이 작으면 답을 찾을 수 없는 경우임
    if scoville[0] < K:
        return -1
    
    
    
    



#################################### 힙(heap) 완벽 이해 ###########################################
# 힙은 정렬되지 않은 리스트에서 최소 값을 먼저 추출해주는 구조

# 정렬되지 않은 배열에서 k번째로 큰 요소 추출
nums = [4,1,7,3,8,5] 
k = 3

heap = list()
for n in nums:
    heapq.heappush(heap, n)


print(heap)
>>> [1, 3, 5, 4, 8, 7]


for _ in range(len(nums)-k):  # 0,1,2 차례로 pop
    heapq.heappop(heap)    
    
print(heap)    
>>> [5,7,8]

print(heapq.heappop(heap))
>>> 5



## heapiy 이용
heapq.heapify(nums)

for _ in range(len(nums)-k):
    heapq.heappop(nums)
    
print(heapq.heappop(nums))
>>> 5


## 최대 힙
# 힙에 튜플(tuple)를 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

print(heap)
>>> [(-8, 8), (-7, 7), (-5, 5), (-1, 1), (-3, 3), (-4, 4)]

while heap:
  print(heapq.heappop(heap)[1])  # 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값을 취하면 됨 (우선순위에는 관심 x)

print(heap)
>>> 8 7 5 1 3 4





