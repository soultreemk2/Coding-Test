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

---------------------------------------------------------------------------------------------------------

# 소수 찾기
from itertools import permutations

def solution(numbers):
    # 소수 판별함수
    def is_prime_number(x):
        if x == 1:
            return False
        else:
            for i in range(2, x):
                if x % i == 0:   # 자기자신보다 작은 모든 수로 나눌때
                    return False # 나누어떨어지는게 하나라도 존재하면 소수가 아님(false)
        return True 
    
    per_list = []
    per_list_final = []
    for i in range(len(numbers)):
        for p in list(permutations(numbers,i+1)):
            per_list.append(''.join(list(map(str,p))))
            per_list_final = list(set(per_list))
    # permutation으로 numbers에서 만들수 있는 모든 숫자의 조합을 append
    ## set으로 중복요소 제거
    
    temp = []
    for i in per_list_final:
        if i.startswith('0'):
            temp.append(i)
            per_list_final = list(set(per_list_final) - set(temp))
    # 예외처리 - 이때 맨 앞에 0이 오는 숫자는 리스트에서 제거
    
    answer = 0
    for num in per_list_final:
        if is_prime_number(int(num)):
            answer += 1

    return answer
    # 해당 리스트에서 소수인 것들의 갯수만 count
    
  
---------------------------------------------------------------------------------------------------------

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


