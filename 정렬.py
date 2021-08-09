# k번째 수
def solution(array, commands):
    answer = []
    
    for c in commands:
        i,j,k = c[0],c[1],c[2]
        answer.append(sorted(array[i-1:j])[k-1])
        
    return answer
  
  
  
  # 가장 큰 수
  
  
  
  
  
  
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
  
  
  
######################### sorted 함수의 다양한 옵션 (key) ######################################
  
  
  
  
