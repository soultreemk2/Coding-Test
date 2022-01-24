 str = input()
 result = [0]*26
 for i in range(str):
    result[ord(i) - 97] = str.count(i)
    
 ## 출력
 for i in result:
    print(i, end=" ")
  
  
 ############################################
 result = list(str(A*B*C))  # ['1','3','3','0','5','3']
 for i in range(10):
 print(result.count(str(i))
       
 ################## 두 수의 합 ##########################
 # 투 포인터 
 arr = list(map(int, sys.stdin.readline().split()))
 X = int(input())
 arr.sort()
     
 left, right = 0, N-1
 ans = 0
 
 while left < right:
       tmp = arr[left] + arr[right]
       if tmp == X:
          ans += 1
          left += 1
       elif tmp < X:
          left += 1
       else:
          right =- 1
       
