# 배낭 문제
cargo = [
    (4,12),
    (2,1),
    (10,4),
    (1,1),
    (2,2)
]

def knapsack(cargo):
    capacity = 15
    pack = []

    # 단가가 높은 순대로 나열
    for c in cargo:
        pack.append((c[0]/c[1],c[0],c[1]))
        pack.sort(reverse=True)

    # 단가 순 그리디 계산
    total_value: float = 0    
        
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            total_value += p[1]*fraction
            break

    return total_value

----------------------------------------------------------------------------------

# 주식 팔고사기 좋은 시점 2
def stock2(stock):
    profit = []
    for i in range(len(stock)-1):
        if stock[i] < stock[i+1]:
            profit.append(stock[i+1] - stock[i])
    return sum(profit)
  
## 다른 풀이
# 매번 이익 계산해 0보다 크면 무조건 합산
def stock3(stock):
  return sum(max(stock[i+1] - stock[i], 0) for i in range(len(stock)-1))

----------------------------------------------------------------------------------

# 키에 따른 대기열 재구성
## 이해 못함. 다시 풀기
  

  
  
  
  
----------------------------------------------------------------------------------
# 태스크 스케줄러
## 이해 못함. 다시 풀기

def scheduler(tasks):
    counter = collections.Counter(tasks)
    result = 0

    while True:
        sub_count = 0

        for task, _ in counter.most_common(n+1):
            sub_count += 1
            result += 1

            counter.subtract(task)
            # 0 이하 아이템을 목록에서 완전히 제거
            counter += collections.Counter()

        if not counter:
            break
        
        result += n - sub_count + 1
        
    return result



  
----------------------------------------------------------------------------------
# 쿠키 부여

def coockies(g, s):
    g.sort()
    s.sort()
    
    i = j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]: # 크기 만족 --> 다음 아이 판단을 위해 i+1
            i += 1       # 만족한 아이 수 count
        j += 1           # 쿠키도 다음 쿠키로 j+1
                         ## 만일 아이가 크기만족 못하면(if문 만족x) --> 아이는 그대로 두고 쿠키만 그 다음 쿠키로 재판단
    return i


