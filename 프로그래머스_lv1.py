# 신고결과 받기
from collections import defaultdict

def solution(id_list, report, k):
    
    dict_list = defaultdict(list)
    ndict = defaultdict(int)
    suspended = [] # 정지된 id
        
    for r in set(report):
        do_report, be_reported = r.split() # 신고한 사람, 신고받은 사람

        # dict로 변경 -> key(신고한 사람)별로 list(신고받은사람) 요소 묶기 - defaultdict
        dict_list[do_report].append(be_reported)
        ndict[be_reported] += 1  # 몇번 신고받았는지 counting

        if ndict[be_reported] == k:
            suspended.append(be_reported)


    answer = [0] * len(id_list)
    for key, value in dict_list.items():   
        for s in suspended:
            if s in value:
                answer[id_list.index(key)] += 1
                
    return answer
  
------------------------------------------------------------------------------------------------------------------------------------ 
# 로또의 최고 순위와 최저 순위
import collections
def solution(lottos, win_nums):
    answer = [0,0]
    rank = [6,6,5,4,3,2,1]
    
    # 최저순위
    cnt_low = 0 # 최저갯수
    for i in lottos:
        if i in win_nums:
            cnt_low += 1
            
    answer[1] = rank[cnt_low]
        
    # 최고순위
    ## 최저갯수 + 0인게 모두 당첨번호라고 가정
    cnt_high = cnt_low + collections.Counter(lottos)[0]
    answer[0] = rank[cnt_high]
    
    return answer
  
------------------------------------------------------------------------------------------------------------------------------------
# 신규아이디 추천
노가다 문제 - 패스

------------------------------------------------------------------------------------------------------------------------------------
# 숫자문자열과 영단어
def solution(s):
    dic = {0:'zero', 1:'one', 2:'two', 3:'three',
           4:'four', 5:'five', 6:'six', 7:'seven',
           8:'eight', 9:'nine'}
    
    for i in dic:
        if dic[i] in s:
            s = s.replace(dic[i], str(i))
    
    return int(s)

------------------------------------------------------------------------------------------------------------------------------------
# 키패드 누르기
def solution(numbers, hand):
    answer = ''
    
    dic = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
           '4': (1, 0), '5': (1, 1), '6': (1, 2),
           '7': (2, 0), '8': (2, 1), '9': (2, 2),
           '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    
    # 키패드간 거리는 가로길이차이 + 세로길이차이
    def dist(num1,num2):
        return abs(dic[num1][0] - dic[num2][0]) + abs(dic[num1][1] - dic[num2][1])
        

    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]:
            answer += "L"
            left_now = i           # 맨 마지막에 위치한 L의 위치 (현재 왼손 위치)
            
        elif numbers[i] in [3,6,9]:
            answer += "R"
            right_now = i          # 맨 마지막에 위치한 R의 위치 (현재 오른손 위치)
        else:
            if dist(numbers[right_now], numbers[i]) < dist(numbers[left_now], numbers[i]):
                answer += "R"
                right_now = i 
                
            elif dist(numbers[right_now], numbers[i]) > dist(numbers[left_now], numbers[i]):
                answer += "L"
                left_now = i
            else:
                answer += hand[0].upper()
                
    return answer

------------------------------------------------------------------------------------------------------------------------------------
# 크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for i in range(len(board[0])):
            if board[i][m-1] != 0:
                stack.append(board[i][m-1])
                board[i][m-1] = 0

                if len(stack) > 1 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break  # 안쪽for문 빠져나옴 -> 다음 m으로 넘어가기
    return answer
  
------------------------------------------------------------------------------------------------------------------------------------
# 음양 더하기
def solution(signs, absolutes):
    answer = 0
    for a,b in list(zip(absolutes, signs)):
        if b == "false":
            a = -a
        answer += a
    return answer

------------------------------------------------------------------------------------------------------------------------------------
# 소수만들기



------------------------------------------------------------------------------------------------------------------------------------
# 실패율
def solution(N, stages):
    People = len(stages)
    faillist = {} # 애초에 딕셔너리로 시작
    for i in range(1, N + 1):
        if People != 0:
            faillist[i] = stages.count(i) / People
            People -= stages.count(i)
        else:
            faillist[i] = 0

    return sorted(faillist, key=lambda i: faillist[i], reverse=True)


