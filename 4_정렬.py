# k번째 수
def solution(array, commands):
    answer = []
    
    for c in commands:
        i,j,k = c[0],c[1],c[2]
        answer.append(sorted(array[i-1:j])[k-1])
        
    return answer
  
----------------------------------------------------------------------------------------------
  
# 가장 큰 수
## 다시 풀기
  
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

----------------------------------------------------------------------------------------------

# H-index

# h번 이상 인용된 논문의 개수 couting (count_1) & 해당 논문 list에 담기 (list_1)
# h번 이상 인용되지 않은 논문: list_2 = citations - list_1 

# 1. count_1 > h
# 2. list_2 내의 모든 요소가 h 이하여야 함

# 1,2번 조건을 만족하는 h값들 중 가장 큰 값을 return


### 시간 초과
def solution(citations):
    citations.sort()
    h = 0
    h_list = []
    
    while h < citations[-2]:
        count_2 = 0
        for i in range(len(citations)):
            if citations[i]>=h:
                count_1 = len(citations[i:])
                break

        for n in citations[:i-1]:
            if n <= h:
                count_2 += 1

        if count_1 >= h and count_2 == len(citations[:i-1]):
            h_list.append(h)

        h += 1
    return max(h_list)


### 시간 초과

def solution(citations):
    citations.sort()
    h = 0
    h_list = []
    
    while h < citations[-2]:
        for i in range(len(citations)):
            if citations[i]>=h:
                count_1 = len(citations[i:])
                break

        if count_1 >= h :
            h_list.append(h)
            
        h += 1
        
    return max(h_list)


## 문제해결 접근 자체가 너무 복잡했음. h값을 하나씩 증가하는 접근 --> for i in range(len(citations))
# 정답 풀이1
def solution(citations):
  sorted_citations = sorted(citations, reverse=True)
  for i in range(len(sorted_citations)):
    if sorted_citations[i] <= i: 
      return i
  return len(sorted_citations)


# 정답 풀이 2


def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
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
  
  

 
  
