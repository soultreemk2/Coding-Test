# k번째 수
def solution(array, commands):
    answer = []
    
    for c in commands:
        i,j,k = c[0],c[1],c[2]
        answer.append(sorted(array[i-1:j])[k-1])
        
    return answer
  
  
  
# 가장 큰 수
## 다시 풀기
  
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))




# 




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
    
    
    while arr[i-1] >= arr[j]:
        j -= 1
    
    arr[i-1],arr[j] = arr[j],arr[i-1]
    
    return arr[0:i] + sorted(arr[i:])
  
  
  
  
  
############################# list, map 함수 #####################################

# map은 리스트의 요소를 지정된 함수로 처리
## 리스트의 모든 실수를 정수로 변환하려면
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
  a[i] = int(a[i])

# map함수를 쓰면
a = list(map(int, a))
  
# 0~9까지의 숫자를 문자열로 변환
a = list(map(str, range(10)))
>>> a : ['0','1','2', ........ , '9']
  
  
  
######################### sorted 함수의 key 옵션 ######################################
 
# 제곱 수가 가장 작은 순서대로 sorting    
a = [ -1, -8, 3, -4, 2, 5, -7]
sorted(a, key=lambda x : x*x, reverse=False) 
print(a)
>>> [-1,2,3,-4,5,-7,8]  

# 튜플 정렬
a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]

c = sorted(a, key = lambda x : x[0]) 
>>> c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

d = sorted(a, key = lambda x : x[1]) 
>>> d = [(3, 0), (5, 1), (0, 1), (1, 2), (5, 2)]



  
  
