#code test

#힙



## 1. 더 맵게
### 1
def solution(scoville, K):
    answer=[]
    final=0
    for i in scoville:
        if i >= K:
            answer.append(i)
            scoville.remove(i)
    scoville.sort()
    scoville.reverse()      #내림차순
    
    if len(scoville)>=2:
        while True:
            a=scoville[-1] + scoville[-2]*2
            final += 1
            if a >= K:
                answer.append(a)
                scoville.remove(scoville[-2])
                scoville.remove(scoville[-1])
            else:
                scoville.remove(scoville[-2])
                scoville.remove(scoville[-1])
                scoville.append(a)
        
            if len(scoville) < 2:
                break
    
    else:
        b = scoville[1] + min(answer) *2
        final += 1
        answer.append(b)
        answer.remove(min(answer))
    
    
    return final
            
            
