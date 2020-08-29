#code test

#해시


## 1. 완주하지 못한 선수
### 1 답은 맞지만 효율성이 낮음.
def solution10(participant, completion):
    for ppl in completion:              #comp에 있는 ppl에 대해
        if ppl in participant:          #만약에 ppl이 part에 있으면
            participant.remove(ppl)     #part에서 해당 ppl 삭제
        else:                           #part-comp
            pass
    return participant[0]    




### 2
def solution11(participant, completion):
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
def solution12(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]




### 4
def solution13(participant, completion): 
    participant.sort() 
    completion.sort() 
    for i in range(len(completion)): 
        if participant[i] != completion[i]: 
            return participant[i] 
    return participant[i+1]









## 2. 전화번호 목록
### 1
### https://assaeunji.github.io/python/2020-05-08-pgphone/
def solution20(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer




### 2
def solution21(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True









## 3. 위장
### 1 이진명
from collections import defaultdict
def solution30(clothes):
    hash_table = defaultdict(int)
    same_type = set()
    answer = 1
    for i in range(len(clothes)):
        cloth = clothes[i][1]
        same_type.add(clothes[i][0])
        for j in range(len(clothes)-1): 
            j += 1
            if cloth == clothes[j][1]:
                same_type.add(clothes[j][0])
        if hash_table[cloth] == 0:
            hash_table[cloth] = list(same_type)
        same_type = set()
    cloth_list = list(hash_table.values())
    #경우의 수 계산
    for i in range(len(cloth_list)):
        answer *= (len(cloth_list[i]) + 1)
    answer -= 1
    return answer




### 2 송민근
from collections import defaultdict
def solution31(clothes):
    hash_table = defaultdict(list)
    answer = 1
    for i, v in clothes:
        hash_table[v].append(i)
    #hash_table에 만들고
    #경우의수 계산
    for i in hash_table.keys():
        answer *= len(hash_table[i])+1
        
    return answer -1
        








## 4. 베스트앨범
### 1. 그룹별로 정렬할 때 계속 역순으로 나와서 문제.
def solution40(genres, plays):
    import pandas as pd
    answer=[]
    df=pd.DataFrame(zip(range(len(genres)),genres,plays))
    df.columns=['a','genres','plays']
    grp=df.groupby('genres')
    df=df.loc[grp[['plays']].transform(sum).sort_values('plays', ascending=False).index]
    df=df.groupby('genres').apply(lambda x: x.nlargest(2, 'plays'))
    #데이터프레임 원래 상태로 되돌림
    df=df.reset_index(0, drop=True)
    asd=list(df['a'])
    asd.reverse()
    
    qwe=list(df['genres'])
    qwe.reverse()

    op=[1]
    #장르 별 곡수가 2개 이상이면 되지만 1개면 문제생김
    
    for i in range(len(qwe)-1):
        if qwe[i] == qwe[i+1]:
            op[-1]+=1
        else:
            op.append(1)
    def covert(asd, op):
        idx = 0
        for v in op: 
            yield asd[idx : idx + v] 
            idx += v 

    zxc=list(covert(asd,op))    
        
    for i in zxc:
        i.reverse()
    for i in zxc:
        answer += i
        
    return answer









### 2. 딕셔너리
from collections import defaultdict
def solution41(genres, plays):
    v1 = defaultdict(int)
    v2 = defaultdict(list)
    answer = []
    for i in range(len(genres)):
        v1[genres[i]] += plays[i]
    genre = [i[0] for i in sorted(v1.items(), reverse = True, key = lambda item : item[1])]
    for i in genre:
        v2[i] = sorted(list(filter(lambda x: genres[x] == i, range(len(genres)))),\
                 key = lambda y : plays[y], reverse=True)
    v3 = list(v2.values())
    for i in range(len(v3)):
        if len(v3[i]) >= 2:
            answer.append(int(v3[i][0]))
            answer.append(int(v3[i][1]))
        else:
            answer.append(int(v3[i][0]))
    return answer
    





























