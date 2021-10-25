#Module 8 HW
#Prof Fried 
#Oct 20, 2021
#Written by Tanner McCarthy

import random as r

#part 1
def avg2Nums(x, y):
  return(x + y)/2

#part2
def sumxtoy(x, y):
  total = 0
  for i in range(x, y + 1):
    total += i
  return total

#part 3
def totalCost(cost, percentOff, tax):
  total = 0
  perOff = (cost * percentOff)
  total = cost - perOff 
  addTax = cost * tax
  total = cost + addTax
  return total

def isPrime(num):
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

#part 4
def listPrimes(x,y):
  for i in range(x, y+1):
    if isPrime(i):
      print(i, end = " | ")

listPrimes(2, 1000)

#part 5
#Test to see if numbers are coPrime 
def coPrimeTest(num1, num2):
  for i in range(2, num2 + 1):
    if num1 % i == 0 and num2 % i == 0:
      return False
  return True

#Q6
def listCoprimes(x):
  print(1)
  for i in range(2, x):
    if coPrimeTest(x, i):
      print(i)

#list twin primes
def isTwinPrimes(x):
  if isPrime(x) and isPrime(x + 2):
    return True
  return False

#Q7
def listTwinPrimes(x, y):
  for i in range(x, y +1):
    if(isTwinPrimes(i)):
      print(i, " ", i + 2)
      i += 2


#test Rock paper scissors game Q8
def rps():
  rockCount = 0
  paperCount = 0
  scissorsCount = 0

  for i in range(10000):
    num1 = r.randint(1, 3)
    num2 = r.randint(1, 3)
    if num1 == num2:
      continue
    elif num1 == 1 and num2 == 2:
      paperCount += 1
    elif num1 == 1 and num2 == 3:
      rockCount += 1
    elif num1 == 2 and num2 == 3:
      scissorsCount += 1

  print("rock ", rockCount/10000)
  print("paper ", paperCount/10000)
  print("scissors ", scissorsCount/10000)


print("\n")

listCoprimes(12)

print("\n")
listTwinPrimes(2, 200)

print("\n")



rps()