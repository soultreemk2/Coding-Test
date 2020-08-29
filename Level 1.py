# 코딩 테스트 LEVEL 1

## 1. 수포자
### 1
def solution10(answers):
    winner=[]
    #패턴
    fir=[1,2,3,4,5]
    sec=[2,1,2,3,2,4,2,5]
    thi=[3,3,1,1,2,2,4,4,5,5]
    #점수
    fir_s=0
    sec_s=0
    thi_s=0
    #정답매칭
    for num in range(len(answers)):      #길이와 문항개수 매칭
        if answers[num] == fir[num%len(fir)]:   #답지의 num = fir의 num, fir은 반복해야 하는 것을 나머지를 통해 표현
            fir_s += 1
        if answers[num] == sec[num%len(sec)]:
            sec_s += 1
        if answers[num] == thi[num%len(thi)]:
            thi_s +=1       #+= 은 왼쪽 변수에 오른쪽 값을 더하고 결과를 왼쪽변수에 할당 (할당 연산자)
    tot_s = [fir_s,sec_s,thi_s]
    
    #max score
    for person, score in enumerate(tot_s):      #반복문 사용시 몇 번째 반복문인지 확인
        if score == max(tot_s):            #매칭 시킨 것 중에 제일 높은 점수
            winner.append(person+1)        #append를 통해 비어있는 winner에 자리수는 0을포함하기 때문에 +1
    
    return winner




### 2
from itertools import cycle
def solution11(answers):
    winner=[]
    #패턴
    fir=[1,2,3,4,5]
    sec=[2,1,2,3,2,4,2,5]
    thi=[3,3,1,1,2,2,4,4,5,5]
    tot_s=[0,0,0]
    
    for fir_s, sec_s, thi_s, answer in zip(cycle(fir),cycle(sec),cycle(thi),
                                           answers):
        if fir_s == answer:
            tot_s[0]+=1
        if sec_s == answer:
            tot_s[1]+=1
        if thi_s == answer:
            tot_s[2]+=1
    for i, score in enumerate(tot_s):
        if score == max(tot_s):         #제일 높은 점수가 score일 때
            winner.append(i+1)          #비어있는 winner에 자리수 0을 포함하기때문에 +1
    return winner




### 3
def solution12(answers):
    p=[[1,2,3,4,5],
       [2,1,2,3,2,4,2,5],
       [3,3,1,1,2,2,4,4,5,5]]
    s=[0]*len(p)            #len(p)는 3, s는 [0,0,0]
    
    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] +=1
    return [i+1 for i, v in enumerate (s) if v ==max(s)]









## 2. 가운데 글자 반환
### 1
def solution20(s):
    if len(s) % 2==1:       #나머지가 1일 때
       return s[len(s)//2]  #[길이/2 의 몫]
    else:
       return s[(len(s)//2-1):len(s)//2+1]  #[길이/2



### 2
def solution21(str):
    return str[(len(str)-1)//2:len(str)//2+1]









## 3. 완주하지 못한 선수
### 1 답은 맞지만 효율성이 낮음.
def solution30(participant, completion):
    for ppl in completion:              #comp에 있는 ppl에 대해
        if ppl in participant:          #만약에 ppl이 part에 있으면
            participant.remove(ppl)     #part에서 해당 ppl 삭제
        else:                           #part-comp
            pass
    return participant[0]    




### 2
def solution31(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for i in participant:            #part에 있는 i에 대해
        dic[hash(i)] = i             #hash함수의 정의를 i로 한다.(i넣으면 i나옴)
        temp += int(hash(i))         #temp에 우변에 있는 것을 더함.
    for v in completion:             #comp에 있는 v에 대해
        temp -= hash(v)              #temp에 우변에 있는 것을 뺌(우변=완주한 선수 명단)
    answer = dic[temp]               #미완주명단을 answer에 넣고

    return answer




### 3
#### 애초에 한명만 완주하지 못했다는 전제가 있어서 가능 여러명일경우 안됨
import collections
def solution32(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]




### 4
def solution33(participant, completion): 
    participant.sort() 
    completion.sort() 
    for i in range(len(completion)): 
        if participant[i] != completion[i]: 
            return participant[i] 
    return participant[i+1]









## 4. k번째수
### 1
def solution40(array, commands):
    answer = []
    for a in commands:
        i, j, k = a[0], a[1], a[2]
        sl = array[i-1:j]            
        sl.sort()                    #정렬
        answer.append(sl[k-1])       #답에 붙여넣기(인덱싱)
    return answer




### 2 람다함수, map함수 사용
def solution41(array, commands):
    #map의 결과를 list로 반환
    #map(함수, 함수 적용할 것)
    return list(map(
        lambda x:
            #x에 ijk를 넣어서 x[0]은 i, x[1] 은 j 
            #i번째 j번째 자른걸 정렬
            sorted(array[x[0]-1 : x[1]])
            #정렬된거 j-1개 반환(0포함하므로 -1하는 것)
            [x[2]-1], commands))   
        




### 3
def solution42(array, commands):
    answer = []
    for a in commands:
        i,j,k = a
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer









## 5. 2016년
### 1
def solution50(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #1월1일은 금요일이니깐 몫이 1일땐 금요일
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    #5월24일이 주어지면 1~4월에 대해서는 months에 해당되어있는 날짜수 더함
    #24일에 대해서는 7로 나눠서 몫 반환한걸 -1해서 번째
    #즉 months[:a-1])+b)%7-1)] 이런 형식도 답이다 (-1을 뒤로 뺌)
    return days[(sum(months[:a-1])+b-1)%7]









## 6. 두 정수 사이의 합
### 1
def solution60(a, b):
    return (abs(a-b)+1)*(a+b)//2    #abs = 절댓값 // = 나누고 소수점 없앰
    
    
    
    
### 2
def solution61(a, b):
    if a > b: a, b = b, a       #b가 무조건 큰수로 지정
    return sum(range(a,b+1))    #a~b까지의 합을 리턴




### 3
    def adder(a, b):
        return sum(range(min(a,b),max(a,b)+1))
    
    
    
    





## 7. 수박수박수박수박수박?
### 1
def solution70(n):
    if n%2==0:                         #=쓰면 안됨
        return '수박'*(n//2)           #/ 쓰면 안됨
    else:
        return '수박'*(n//2)+'수'      #/쓰면 안됨
        
    
    
    
### 2 (1, 2번은 두배한 것에 수를 더함)
def solution71(n):
    return "수박"*(n//2) + "수"*(n%2)




### 3
def solution72(n):
    s = "수박" * n
    return s[:n]




### 4 (3, 4번은 길이보다 크게 해서 필요한 길이만큼 추출)
def solution73(n):
    return ("수박"*n)[0:n]









## 8. 서울에서 김서방 찾기
### 1
def solution80(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))




### 2
def solution81(seoul):
    return '김서방은 '+str(seoul.index('Kim'))+'에 있다'       #str은 해당 내용을 문자열로반환




### 3
def solution82(seoul):
    return ('김서방은 %d에 있다' %seoul.index('Kim'))









## 9. 문자열을 정수로 바꾸기
### 1
def solution90(s):
    return int(s)




### 2
def solution91(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result









## 10. 같은 숫자는 싫어
### 1
def solution100(s):
    a = []          #빈 배열만들고
    for i in s:     #s에 있는 숫자들에 i 부여
        if a[-1:] == [i]: continue      #빈 배열과 i를 비교
        #b[-1:] , b[-1] 차이 주의
        a.append(i)                     #
    return a









## 11. 약수의 합
### 1
def solution110(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    return answer




### 2
def solution111(n):
    #자신도 약수니깐 n 기본으로 넣고
    #1 부터 n의 절반+1 까지(약수의 조합은 어차피 절반만 보면댐)
    #조건 = 몫이 0일때, 
    return n + sum([i 
                    for i in range(1, (n // 2) + 1) 
                    if n % i == 0])









## 12. 짝수와 홀수
### 1
def solution120(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"




### 2
def solution121(num):
    if (num%2):         #num%2 = 1일때 즉 참일 때
        return "Odd"
    else:
        return "Even"
    
    
    
    
    
    
    
    
    
## 13. 평균 구하기
### 1
def solution130(arr):
    v=0
    for i in arr:
        v = v + i
    return v/(len(arr))




### 2
def solution131(arr):
    return (sum(arr) / len(arr))









## 14. 핸드폰 번호 가리기
def solution140(phone_number):
    return "*"*(len(phone_number)-4)+phone_number[-4:]









## 15. 행렬의 덧셈
### 1 zip함수 = 동일한 개수로 이루어진 자료형을 묶어주는 역할
def solution150(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer
    



### 2
def solution151(arr1, arr2):
    tmp = []
    answer = []
    for a, b in zip(arr1, arr2):   # 1번째 for문
        for c,d in zip(a,b):        # 2번째 for문
            tmp.append(c+d)
        answer.append(tmp)
        tmp = []
    return answer
    



### 3
def solution152(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A




### 4
import numpy as np
def solution153(A,B):
    A=np.array(A)           #np.array사용하면 행렬의 합 바로 계산 가능
    B=np.array(B)
    answer=A+B
    return answer.tolist()  #다시 np.array한것을 리스트 형식으로 









## 16. 자릿수 더하기
### 1
def solution160(number):
    if number < 10:         #10이하의 수면 바로 그 수 반환
        return number;
    #number%10= 첫번째 자리수, 뒷부분은 10으로 나누면서 계속 두번쨰 세번째 자리 숫자 +
    return (number % 10) + solution160(number // 10)    




### 2
def solution161(number):
    return sum([int(i) for i in str(number)])




### 3
def solution162(number):
    return sum(map(int,str(number)))









## 17. 나누어 떨어지는 숫자 배열
### 1   
def solution170(arr, divisor):
    answer = []
    for i in range(len(arr)) :
        if arr[i] % divisor == 0 :
            answer.append(arr[i])
    if len(answer) == 0 :
        answer.append(-1)
    else :
        answer.sort()
    return answer
            



### 2
def solution171(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
    



### 3
def solution172(arr, divisor):
    arr = [x for x in arr if x % divisor == 0];
    arr.sort();
    return arr if len(arr) != 0 else [-1];









## 18. 문자열 내 p와 y의 개수
def solution180(s):
    #lower = 다 소문자로 바꾸고 카운트
    return s.lower().count('p') == s.lower().count('y')









## 19. 문자열 다루기 기본
### 1
def solution190(s):
    #숫자인지 확인 and 길이가 4~6인지 확인
    return s.isdigit() and len(s) in (4, 6)









## 20. 문자열 내림차순으로 배치하기
### 1
def solution200(s):
    #sorted부분만 있으면 리스트만 반환
    return ''.join(sorted(s, reverse=True))









## 21. 크레인 인형뽑기 게임
### 1
def solution210(board, moves):
    a = []
    answer = 0
    for i in moves:
        for j in range(len(board)):     #range(len()) range(0,높이)
            if board[j][i-1] != 0:      #x,y좌표 지정한곳이 0이 아니면
                a.append(board[j][i-1]) #해당 위치에 있는 숫자를 a(바구니)에 추가
                board[j][i-1] = 0

                if len(a) > 1:
                    if a[-1] == a[-2]:
                        a.pop(-1)
                        a.pop(-1)
                        answer += 2     
                break

    return answer









## 22. 체육복 
## (중복이 없다=lost, reverse내의 원소값은 unique)
## (여벌의 체육복이 있는 학생도 도난 가능성 있)
### 1
def solution220(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:           #여벌 있는 애를 i
        if i-1 in set_lost:         #i의 왼쪽에 잃어버린 애가 있으면
            set_lost.remove(i-1)    #잃어버린애 리스트에서 i-1 제거
        elif i+1 in set_lost:       #i의 오른쪽에 잃어버린 애가 있으면
            set_lost.remove(i+1)    #잃어버린애 리스트에서 i+1 제거
    return n - len(set_lost)        #전체 인원에서 못빌린수 빼기









## 23. 문자열 내 마음대로 정렬하기
### 1
def solution230(strings, n):
    return sorted(sorted(strings) ,key=lambda x: x[n])      #왜 sorted 두번?









## 24. 소수 찾기 (에라토스테네스의 체 사용)
### 1
def solution240(n):
    num=set(range(2,n+1))       #2~n까지의 수

    for i in range(2,n+1):
        if i in num:
            #set(range(a,b,c))=a~b 사이의 a, a+c, a+2c, a+3c ...
            num-=set(range(2*i,n+1,i))   
    return len(num)
                








## 25. 시저 암호
## ord() a~z : 97~122, A~Z : 65~90
## chr() 위 숫자 넣으면 문자 반환
### 1
def solution250(s, n):
    s = list(s)         #각 자리수마다 리스트로
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+n)%26+ord('a'))
    return ''.join(s)
            








## 26. 이상한 문자 만들기
### 1
def solution260(s):
    res = []
    for x in s.split(' '):  #공백을 기준으로 단어를 나눔
        word = ''
        for i in range(len(x)): #각 단어x의 자리수를 i로
            c = x[i].upper() if i % 2 == 0 else x[i].lower()
            word = word + c
        res.append(word)
    return ' '.join(res)
    



### 2
def solution261(s):
    return ' '.join([''.join([c.upper() 
                              if i % 2 == 0 
                              else c.lower() 
                              for i, c in enumerate(w)]) 
                     for w in s.split(' ')])









## 27. 자연수 뒤집어 배열로 만들기
### 1
def solution270(n):
    a = list(str(n))        #str 왜 필요한지
    a.reverse()
    
    return list(map(int, a))




### 2
def solution271(n):
    return list(map(int, reversed(str(n))))
    








## 28. 정수 내림차순으로 배치하기
### 1
def solution280(n):
    #sorted 와 str 사이에 list 안넣어도됨, sorted가 리스트로 변환해줌
    return int(''.join(sorted(str(n), reverse=True)))









## 29. 정수 제곱근 판별
### 1
def solution290(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:   #루트 씌운게 정수이면
        return (sqrt + 1) ** 2
    return -1




### 2
def solution291(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or -1









## 30. 제일 작은 수 제거하기
### 1
def solution300(arr):
    if len(arr)>1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]
    
    
    
    
### 2
def solution301(arr):
    return [i for i in arr if i > min(arr)]









## 31. 최대공약수와 최소공배수 
### 1
def solution310(n, m):
    #n의 약수
    a = [i for i in range(1,n+1) if n%i==0]
    b = [i for i in range(1,m+1) if m%i==0]

    c = max([i for i in a if i in b])
    d = c*(n/c)*(m/c)
    answer = [c, d]
    return answer




### 2
def solution(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer









## 32. 콜라츠 추측
def solution320(num):
    answer = 0
    while num!=1:       #num이 1이 아니면
        if num%2==0:    #2의 배수일때
            num=num/2   #2로 나눈다
        else:           #홀수이면
            num=3*num+1 #3을 곱하고 1을 더한다
        answer=answer+1 #이 과정이 한번 끝나면 answer에 1 추가

        if answer>=500: #500번이상 해야한다면
            return -1   #-1을 반환

    return answer









## 33. 하샤드 수
### 1
def solution(x):
    for i in range(len(str(x))):
        if x%sum(int(x[i]))==0:
            return 'true'
        else:
            return 'false'
        
        
        
        
### 2
def solution331(n):
    return n % sum([int(c) for c in str(n)]) == 0




### 3
def solution332(n):
    st = str(n)
    a = 0
    for i in range(len(st)):
        a += int(st[i])

    return True if n%a == 0 else False        
        







## 34. x만큼 간격이 있는 n개의 숫자
### 1
def solution340(x, n):
    return [i * x + x for i in range(n)]
    








## 35. 직사각형 별 찍기
### 1
a, b = map(int, input().strip().split(' '))
for i in range(b):            
    for j in range(a):        
        print('*', end='') 
    print()




### 2
a, b = map(int, input().strip().split(' '))
print(("*" * a + "\n") * b)









## 36. 예산
### 1
def solution360(d, budget):
    answer=0
    sum=0
    for i in sorted(d):
        if sum+i<=budget:
            sum+=i
            answer+=1
    return len(answer)




### 2
def solution361(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)









## 37. [1차] 비밀지도
### 1
def solution370(n, arr1, arr2):
    answer=[]
    for i, v in zip(arr1, arr2):
        u = str(bin(i|v)[2:])
        u = u.rjust(n,'0')
        u = u.replace('1','#')
        u = u.replace('0',' ')
        answer.append(u)
    return answer




### 2
def solution371(n, arr1, arr2):
    answer = []
    for i in range (0,n):
        a = format(arr1[i] | arr2[i], str(n)+'b')
        a = a.replace('0',' ')
        a = a.replace('1','#')
        answer.append(a)
    return answer




### 3 미친넘
solution372 = lambda n, arr1, arr2: ([''.join(map(lambda x: '#' if x=='1' else ' ', "{0:b}".format(row).zfill(n))) for row in (a|b for a, b in zip(arr1, arr2))])









## 38. 실패율
def solution(N, stages):
    for i in stages:
        




















    
    








