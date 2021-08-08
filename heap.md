# 더 맵게







#################################### 힙(heap) 완벽 이해 ###########################################
# 힙은 정렬되지 않은 리스트에서 최소 값을 먼저 추출해주는 구조
![image](https://user-images.githubusercontent.com/50647833/128635453-d783bfc0-9834-4061-a4ef-3ca5a7389110.png)


# 정렬되지 않은 배열에서 k번째로 큰 요소 추출
nums = [3,2,3,1,2,4,5,5,6] 
k = 4

heap = list()
for n in nums:
  heapq.heappush(heap, -n)   # heap: [-3,-2,-3,-1,-2,-4,-5,-5,-6]
  
for _ in range(k):           # 가장 작은 k개 (-6,-5,-4,-3) 삭제(pop)
  heapq.heappop(heap)        # heap: [-2,-1]
  
print(-heaq.
