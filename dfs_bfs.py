# 프로그래머스 - 타겟 넘버







# 파알인- 전화번호 문자 조합
## 매우 어렵다..

def letterCombinations(self, digits:str) -> List[str]:
  def dfs(index, path):
    if len(path) == len(digits):
      result.append(path)
      return
    
    for i in range(index, len(digits)):
      for j in dic[digits[i]]:
        dfs(i+1, path+j)
        
   # 예외처리   
   if not digits:
    return []
  
  dic = {"2":"abc", "3":"def", "4":"ghi","5":"jkl",
      "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
  
  result = []
  dfs(0, "")
  
  return result



# 파알인- 조합의 합













# 파알인- 부분 집합
result = []

def dfs(nums, index, path):
    result.append(path)
    
    for i in range(index, len(nums)):
        dfs(nums, i+1, path + [nums[i]])
        
    return result

def solution(nums):
    answer = dfs(nums, 0, [])
    return answer
  
  
>> solutions([1,2,3])
>>> [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]


