## 완전탐색은 간단히 가능한 모든 경우의 수를 다 체크해서 정답을 찾는 방법 (브루트 포스)
# ① Brute Force 기법 - 반복 / 조건문을 활용해 모두 테스트하는 방법
# ② 순열(Permutation) - n개의 원소 중 r개의 원소를 중복 허용 없이 나열하는 방법
# ③ 재귀 호출
# ④ 비트마스크 - 2진수 표현 기법을 활용하는 방법
# ⑤ BFS, DFS를 활용하는 방법



# 모의고사

def solution(answer):
    result = []
    p_1 = list(range(1,6))
    p_2 = [2,1,2,3,2,4,2,5]
    p_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c_1, c_2, c_3 = 0, 0, 0
    
    for i in range(len(answer)):
        if answer[i] == p_1[i%len(p_1)]:
            c_1 += 1
        if answer[i] == p_2[i%len(p_2)]:
            c_2 += 1
        if answer[i] == p_3[i%len(p_3)]:
            c_3 += 1
            
    for i,j in enumerate([c_1,c_2,c_3]):
        if j == max([c_1,c_2,c_3]):
            result.append(i+1)
        
    return result



# 소수 찾기
from itertools import permutations

def solution(numbers):
    # 소수 판별 함수 정의
    def is_prime_number(x):
        if x == 1:
            return False
        else:
            for i in range(2, x):
                if x % i == 0:
                    return False # 소수가 아님

        return True 
    
    
    # 모든 조합의 수 나열
    temp = []
    prime = []
    numbers_all = []

    for i in range(len(numbers)):
        perm = list(permutations(numbers,i+1))
        for j in range(len(perm)):
            numbers_all.append(''.join(perm[j]))
            numbers_final = list(set(numbers_all))  
            ## [0,1,1] 처럼 동일한 숫자가 리스트에 여러번 있을 경우 permutation이 동일한거 여러번 나옴 
            #  --> set 적용

    ## 이때 배열에서 0으로 시작하는 숫자는 제거 (중복방지) 
    
    for n in numbers_final:
        if n.startswith('0'):
            temp.append(n)
            numbers_final = list(set(numbers_final) - set(temp))    
    
    
    # 소수 판별 함수 적용
    result = []
    for num in numbers_final:
        result.append(is_prime_number(int(num)))
    
    return sum(result)



# 카펫

def solution(brown, yellow):
    x_list = []
    y_list = []
    xy_list = []
    result = []
    
    for y in range(1,yellow+1):
        if yellow % y == 0 and yellow // y >= y:
            x_list.append(yellow // y)
            y_list.append(y)

    for i in range(len(x_list)):
        xy_list.append((x_list[i],y_list[i]))

    for xy in xy_list:
        if (xy[0] + xy[1])*2 + 4 == brown and xy[0]*xy[1] == yellow:
            return [xy[0]+2,xy[1]+2]





########################## 소수 판별 알고리즘 ##########################
# 소수란 '1과 자기자신'을 제외한 숫자로 나누어지지 않는 수

def is_prime_number(x):
    if x == 1:
        return False
    else:
        for i in range(2, x): # 2부터 (x - 1)까지의 모든 수를 확인하며
            if x % i == 0:    # x가 해당 수로 나누어떨어진다면
                return False # 소수가 아님
        
    return True # for문에서 if문에 걸러지는게 아무것도 없으면, 즉 1과 자신을 제외한 수로는 나누어지지 않으면 소수임



############### permutation, combination ##########################

from itertools import permutations

a = [1,2,3]
permute = permutations(a,2)

print(list(permute))
>>> [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]


a = [1,2,3]
combi = combinations(a,2)
    
print(list(combi))
>>> [(1,2),(1,3),(2,3)]



#################### 문자열  ##########################
# 문자열 나누기
str = "Hi my name is limcoing" 
splitted_str = str.split() 
print(splitted_str)
>>> ['Hi', 'my', 'name', 'is', 'limcoing'] 

# 문자열 합치기
joined_str = ''.join(splitted_str) 
print(joined_str)
>>> Himynameislimcoing


a = ('1','2','5')
a_join = ''.join(a)
print(a_join)
>>> 125
