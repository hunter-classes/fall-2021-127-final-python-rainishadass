#question 1
l = [2,4,6,8,10,13]
#l = [8,5,4,3]
def isIncreasing(l):
  
  for i in l:
    #if statement should represent the increase after each element
    if i + 1 > 0 :
      print("True")
    
    else:
      print("False")
  

  
#question 2
l2 = [3,5,2,1]
def NumConvert(l2):
#should take nums from list,convert to integer, then return them together
  result = ' '
  for i in l2:
    nums = int[l2]
    print(nums)
  return result 
  
#[for i in l2]
  




#question 3
def BinConvert(str):
#takes a string returns an int
  binary = ["0","1","10","11","100","101"]
  #integer = ["0","1","2","3","4","5"]  

  
    
    
 


print("----- question 1 -----")
print(isIncreasing(l))
print("----- question 2 -----")
print(NumConvert(l2))
print("----- question 3 -----")
print(BinConvert("101"))