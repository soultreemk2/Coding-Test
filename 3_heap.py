# 더 맵게

import heapq

def solution(scoville,K):
    solution = 0
    heapq.heapify(scoville)
        
    while len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        solution += 1
        heapq.heappush(scoville, a+2*b) # 힙정렬 (if문 걸리기 전까지 계속 반복 -> solution도 계속 +1 )

        if scoville[0] >= K:  # 가장 작은 값이 K보다 크면
            return solution
        
    # while문을 다 돌고 난 후에도 (즉 a,b를 heap에 계속 넣어주는 작업을 scoville에 원소가 남아있을 때 까지 무한 반복) 했음에도
    # 첫번째 요소가 k보다 값이 작으면 답을 찾을 수 없는 경우임
    if scoville[0] < K:
        return -1
    
    
    
  
    

------------------------------------------------------------------------------------------------------------------------------------------
# 파알인(456p~)
------------------------------------------------------------------------------------------------------------------------------------------
# 배열의 k번째 큰 요소

import heapq

nums = [4,1,7,3,8,5] 
k = 3

heap = list()
# 1차 힙정렬
for n in nums:
    heapq.heappush(heap, n) # [1,3,5,4,8,7]

# (최소값 추출 -> 힙정렬 -> 최소값 추출) - k번 반복
for _ in range(k): # k번 추출
    heapq.heappop(heap)   

# [1,3,5,4,8,7] -> [3,5,4,8,7]           1번째 작은값 추출
# [3,5,4,8,7] -> [5,4,8,7] -> [4,5,8,7]  2번째 작은 값 추출
# [4,5,8,7]   -> [5,8,7]  ->  [5,7,8]    3번째 작은 값 추출

print(heapq.heappop(nums))
>> 5  # 3번째로 큰 값



## heapiy 이용
heapq.heapify(nums)

for _ in range(len(nums)-k):
    heapq.heappop(nums)
    
print(heapq.heappop(nums))
>>> 5



## 부호 바꿔서
heap = list()
# 1차 힙정렬
for n in nums:
    heapq.heappush(heap, -n) 

for _ in range(k): # k번 추출
    heapq.heappop(heap)   
    
print(-heapq.heappop(heap))


-----------------------------------------------------------------------------------------------
# 상위 k빈도요소

import collections
import heapq

def solution(nums):
    freqs = collections.Counter(nums)
    freqs_heap = list()
    topk = []
    # 최대힙으로 구현하기 위해 -로 삽입
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))
        
    # 총 k번의 최소freq(최대값) pop --> topk에 append
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
    
    return topk


-----------------------------------------------------------------------------------------------
# 라면공장 - 지금은 사라짐
## 다시 풀기

https://johnyejin.tistory.com/74






