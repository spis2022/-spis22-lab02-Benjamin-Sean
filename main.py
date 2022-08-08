# The goal of this program is to practice Python constructs  
import math
   
#while number>0:
#  print(a)


#2. Asking the User for Input
def getNumber():
   result = ""
   number = 0
   while number>=0:
     symbols = input("Enter a digit: ")
     number = int(symbols)
     if number<0:
      return result
     result = result + str(number)
   return result

print(getNumber()) 
   

#3. Getting the Sum of the Digits  
def sumDigits(num):
  sum = 0
  while num>0:
    a = num%10
    sum = sum + a
    num = int(num//10)

  return sum

print(sumDigits(236))


#4. Wage Converter
def convertWageMtoW(mWage, c):
   country = c
   wageGapUS = 0.182
   wageGapJapan = 0.221
   wageGapCanada = 0.167
   wageGapUK = 0.143
   wageGapFrance = 0.118
   wageGapItaly = 0.076
  
   if country == "US":
     ratio = 1 - wageGapUS
   elif country == "Japan":
     ratio = 1 - wageGapJapan
   elif country == "Canada":
     ratio = 1 - wageGapCanada
   elif country == "UK":
     ratio = 1 - wageGapUK
   elif country == "France":
     ratio = 1 - wageGapFrance
   elif country == "Italy":
     ratio = 1 - wageGapItaly
   else:
     return "No data"
     
   return mWage * ratio

#verify
print("A mans wage of 100 in the US is converted to:", round(convertWageMtoW(100, "US"),2))
print("A mans wage of 76.2 in the US is converted to:", round(convertWageMtoW(76.2, "US"), 2))
print("A mans wage of 0 in the US is converted to:", convertWageMtoW(0, "US"))
# test cases
print("A mans wage of 87 in the US is converted to:", round(convertWageMtoW(87, "US"),2))
print("A mans wage of 21 in the US is converted to:", convertWageMtoW(21, "US"))
#Adding and testing additional functionality
print("A mans wage of 100 in Japan is converted to:", convertWageMtoW(100, "Japan"))
print("A mans wage of 100 in Canada is converted to:", convertWageMtoW(100, "Canada"))
print("A mans wage of 100 in the UK is converted to:", convertWageMtoW(100, "UK"))
#test case - no data
print("A mans wage of 100 in the Arctic is converted to:", convertWageMtoW(100, "Arctic"))
