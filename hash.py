def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
    

#### reduce 함수에 대해 정리 ####
## 앞선 계산에 누적해서 계산해줌
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# 10

reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 10)
## initializer에 10을 지정하면 10부터 시작
# 25

reduce(lambda x, y: x*y, range(1, 6))
# 120
