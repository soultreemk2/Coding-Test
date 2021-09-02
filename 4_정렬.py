# k번째 수
def solution(array, commands):
    answer = []
    
    for c in commands:
        i,j,k = c[0],c[1],c[2]
        answer.append(sorted(array[i-1:j])[k-1])
        
    return answer
  
----------------------------------------------------------------------------------------------
  
# 가장 큰 수
## https://jokerldg.github.io/algorithm/2021/05/06/most-big-number.html
  
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))



# 다른 풀이 - 삽입 정렬
class Solution:
    
    # 맨 앞에서부터 자릿수 단위로 비교
    # 즉, 9는 30보다 맨 앞자리 수가 더 크므로 9가 더 앞에 와야함
    # 쉽게 비교하려면 930과 309중 어떤게 더 큰지 비교 --> 더 큰값을 맨 앞으로 swap
  
    def to_swap(n1,n2):
        return str(n1) + str(n2) < str(n2) + str(n1) # true 이면 자리를 바꿔야함
    
    # 1) i-1과 i의 스왑여부를 결정
    # 2) 스왑이 안일어나면 i를 다음 순서로 넘기고
    # 3) 스왑이 일어나면 일어난 지점부터 그 앞에 숫자들까지 다시 전부 스왑을 해주어야함
    # 4) 3) 스텝을 지나면 i를 다음 순서로 넘김
    
    def largestNumber(nums):
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and Solution.to_swap(nums[j-1],nums[j]): # swap이 일어나면 그 앞에 있는 숫자들 전부 다시 비교 
                nums[j-1],nums[j] = nums[j], nums[j-1]  # i는 고정, (j만 움직이기)
                j -= 1
            i += 1 # swap이 안일어나면 (혹은 swap이 이루어진 후 그 앞 문자열까지 다 비교 후에) 다음 판단으로
            
        return ''.join(list(map(str,nums)))


    
# 다른 풀이 - 커스텀정렬(cmp to key)

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
    
    
    
----------------------------------------------------------------------------------------------

# H-index

# citations[i]는 i번 논문이 인용된 횟수
# len(citations) - i는 인용된 논문의 개수를 최댓값부터 하나씩 줄여나간 것이다 (최댓값을 찾아야 하므로 가장 큰 값부터 시작)
def solution(citations):
    answer = []
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i: # h번 인용된 논문이 h편 이상
            return len(citations)-i
    return 0

----------------------------------------------------------------------------------------------

# 추가문제 - leetcode next permutation
# https://jins-dev.tistory.com/entry/%EB%8B%A4%EC%9D%8C-%EC%88%9C%EC%97%B4-%EC%B0%BE%EA%B8%B0-%EC%A0%84%EC%B2%B4-%EC%88%9C%EC%97%B4-%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Next-Permutation
    
def next_permutation(arr):
    i,j = len(arr)-1, len(arr)-1
    
    while i> 0 and arr[i-1]>=arr[i]: # 만족하면 stop임
        i -= 1
    
    if i==0:
        arr.reverse()
        return arr
    elif i == len(arr)-1:
        arr[-1],arr[-2] = arr[-2], arr[-1]
        return arr
    
    
    while arr[i-1] >= arr[j]:  # arr[i-1]이 항상 arr[j] 보다 작다면 j는 그대로 변함없이 len(arr)-1 이 추출
        j -= 1
    
    arr[i-1],arr[j] = arr[j],arr[i-1]
    
    return arr[0:i] + sorted(arr[i:])
  
    
  

## 다른 풀이 - 필패 코드

def next_permutation_2(arr):
    i,j = 0, len(arr)-1
    
    while i < len(arr)-1 and arr[i] < arr[i+1]:   # 이렇게하면 가장 마지막 i가 아니라 맨 앞의 i가 추출되게 됨
        i += 1
    
    if i==0:
        arr.reverse()
        return arr
    elif i == len(arr)-1:
        arr[-1],arr[-2] = arr[-2], arr[-1]
        return arr
    
    
    while arr[i-1] < arr[j]:
        j += 1
    
    arr[i-1],arr[j] = arr[j],arr[i-1]
    
    return arr[0:i] + sorted(arr[i:])



------------------------------------------------------------------------------------------------------------------------------------------
# 파알인(479p~)
------------------------------------------------------------------------------------------------------------------------------------------
# 구간 병합
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    merged = []
    for i in sorted(intervals, key=lambda x:x[0]):
        if merged and i[0] <= merged[-1][1]:
            merged[-1][1] = max(i[1], merged[-1][1])
        else:
            merged += i,
    return merged
    
# merged가 비어있으면 i를 넣어주고 시작해야함
# 따라서 if merged and ~~ 조건을 넣어줌으로써 merged가 비어져있는 초기에 바로 else문으로 넘어가게 함

# [1,8], [2,6] 경우에는 2<8 일지라도 6이 8보다 작으므로 8에 병합되어야함 --> max로 판단
    

------------------------------------------------------------------------------------------------------    
# 색 정렬 
## 투 포인터 --> mid 추가 (쓰리포인터)

def solution(s):
    i, j, k = 0, 0, len(s)
    mid = 1
    
    while j < k:
        if s[j] < mid:   # 오른쪽으로 보내질 필요가 없이 왼쪽 내에서만 움직이면 됨 (i와 swap)
            s[i], s[j] = s[j], s[i]
            i += 1
            j += 1
        
        elif s[j] > mid: # 오른쪽으로 보내야함 (k와 swap)
            k -= 1
            s[j], s[k] = s[k], s[j]
        else:            # swap할 필요 없음 (제 위치에 있는 것 --> j 위치만 증가)
            j += 1 

------------------------------------------------------------------------------------------------------    
# 원점에서 k번째로 가까운 점

def kClosest(points,k):
    temp = []
    for i,p in enumerate(points):
        i = p[0]**2 + p[1]**2
        temp.append([i,p])

    arr = sorted(temp, key=lambda x:x[0])
    answer = []
    for i in range(k):
        answer.append(arr[i][1])

    return answer


## 힙으로도 풀이 가능
# k번 추출 -> 우선순위 큐(힙)로 k번 출력

import heapq

def solution(points, k):
    heap = list()
    for (x,y) in points:
        dist = x**2 + y**2
        heapq.heappush(heap, (dist,x,y))
        
    answer = []
    for _ in range(k): # dist 최소 k개
        (dist,x,y) = heapq.heappop(heap)
        answer.append((x,y))
        
    return answer








    
    
    
    
    
  

 
  
