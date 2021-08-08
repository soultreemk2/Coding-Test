# 더 맵게







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
