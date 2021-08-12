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
        for i in range(2, x):
            if x % i == 0:
                return 0 # 소수가 아님

        return 1 # true이면 소수    
    
    
    # 모든 조합의 수 나열
    temp = []
    prime = []
    numbers_all = []

    for i in range(len(numbers)):
        perm = list(permutations(numbers,i+1))
        for j in range(len(perm)):
            numbers_all.append(''.join(perm[j]))
            numbers_final = list(set(numbers_all))

    ## 이때 배열에서 0으로 시작하는 숫자는 제거 (중복방지) 
    ## & 소수판별함수가 2이상 숫자만 판단 가능하므로 1인 숫자는 제거

    for n in numbers_final:
        if n.startswith('0') or n == '1':
            temp.append(n)
            numbers_final = list(set(numbers_final) - set(temp))    
    
    
    # 소수 판별 함수 적용
    result = []
    for num in numbers_final:
        result.append(is_prime_number(int(num)))
    
    return sum(result)



########################## 소수 판별 알고리즘 ##########################
# 소수란 '1과 자기자신'을 제외한 숫자로 나누어지지 않는 수

def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
        
    return True # for문에서 if문에 걸러지는게 아무것도 없으면, 즉 1과 자신을 제외한 수로는 나누어지지 않으면 소수임


