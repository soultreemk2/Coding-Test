#code test

#정렬



## 1. K번째 수
### 1
def solution10(array, commands):
    answer = []
    for a in commands:
        i, j, k = a[0], a[1], a[2]
        se = array[i-1:j]            #slice 함수 사용(잘라낼 때)
        se.sort()                    #정렬
        answer.append(se[k-1])       #답에 붙여넣기(인덱싱)
    return answer









## 2. 가장 큰 수 
### 1
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    #t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) 

def solution20(numbers):
    #리스트에 있는 숫자들을 스트링으로 변환
    n = [str(x) for x in numbers]
    #
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer



    
### 2
def solution21(numbers):
    #리스트에 있는 숫자들을 스트링으로 변환
    numbers = list(map(str, numbers))
    #3배해서 앞 3글자만 크기 비교 한걸 리버스 (왜 첫 3개의 숫자만 크기  비교하지?)
    numbers.sort(key = lambda x: x*3, reverse=True)
    #해당 리스트 합치기
    return str(int(''.join(numbers)))









## 3. H-index
def solution(citations):
    a=[0]*len(citations)
    for i in range(len(citations)-1):
        for x, j in enumerate(range(len(citations)-1)):
           while True:
               if citations[i]>=citations[j]:
                   a[j]+=1
                   if x == range(len(citations)-1):
                       break
        
            
    
    return max(a)



def solution(citations):
    import itertools
    for i, v in combinations(citations,2):
        
            























