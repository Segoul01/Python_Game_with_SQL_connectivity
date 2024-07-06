# 1.
# n = int(input("Enter number of Lines: "))
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end='')
#     print()
    
# --------------------------------------------------->

# 2.
# n = int(input('Enter number: '))
# for i in range(10):
#     print(f'{n}x{i+1}={n*(i+1)}')

# --------------------------------------------------->

# 3.
# tf is the pattern????????????

# --------------------------------------------------->

# 4.
# n = int(input("Enter number: "))
# fact = 1
# for i in range(2,n+1):  fact *= i
# print(f'{n}! is {fact}')

# --------------------------------------------------->

# 5.
# n = int(input('Enter Number: '))
# rev_n = int(str(n)[::-1])
# print(rev_n)

# --------------------------------------------------->

# 6.
# l = []
# while True:
#     n = int(input("Enter Number: "))
#     if n == 0:  break
#     l.append(n)
# neg_sum = 0
# even_sum = 0
# odd_sum = 0
# for i in l:
#     if i < 0:   neg_sum += i
#     else:
#         if i % 2 == 0:  even_sum += i
#         else: odd_sum += i
# print(f'Sum of negative no.: {neg_sum}')
# print(f'Sum of positive even no.: {even_sum}')
# print(f'Sum of positive odd no.: {odd_sum}')

# ---------------------------------------------------------->

# 7.
# w t f

# ------------------------------------------------------------->

# 8.
# n = int(input("Enter number of Lines: "))
# for i in range(n):
#     print('*'*(i+1))

# --------------------------------------------------------------->

#  S T R I N G S

# 1.
# num = input("Enter phone number: ")
# isValid = True
# if len(num) != 12: 
#     isValid = False
# else:
#     for i in range(12):
#         if (i == 3 or i == 7):
#             if num[i] != '-':  isValid = False
#         elif not num[i].isdigit():  isValid = False
# print(f'Is Valid : {isValid}')

# ---------------------------------------------------------->

# 2.
# a = input("Enter Text: ")
# # a
# print(a)
# # b
# length = len(a)
# print(length)
# # c
# alnum = 0
# alnum_perc = 0
# for i in a:
#     if i.isalnum:   alnum+=1
# alnum_perc = (alnum/length)*100
# print(alnum_perc)

# --------------------------------------------------------->

# 3.
# s = input("enter string: ")
# digits = []
# digits_sum = 0
# hasDigits = False
# for i in s:
#     if i.isdigit(): 
#         digits.append(eval(i))
#         hasDigits = True
# if hasDigits:
#     digits_sum = sum(digits)
#     print(f'Original String: {s}')
#     print(f"Digits: {digits}")
#     print(f'Sum of Digits: {digits_sum}')
# else:
#     print(f'Original String: {s}')
#     print('has no string')

# --------------------------------------------------->

#  T U P L E S

# 1.
# n = int(input("Enter term: "))
# pos = 0
# f = [0,1]
# current = f[-1]
# isValid = True
# while current < n:
#     f.append(f[-1] + f[-2])
#     current = f[-1]
#     if current > n:
#         print("term doesn't exist")
#         isValid = False
#         break
# if isValid: 
#     pos = len(f)
#     print(pos)

# ---------------------------------------------------->

# 2.
# l = eval(input("Enter tuple: "))
# n = int(input("Enter index: "))
# print(l[n])

# ---------------------------------------------------->

# 3.
# seq_a = eval(input("Enter tuple a: "))
# seq_b = eval(input("Enter tuple b: "))
# flag = True
# for i in seq_a:
#     if i not in seq_b:  flag = False
# print(flag)

# ---------------------------------------------------->

# 4.
# f = [0,1]
# for i in range(9):  f.append(f[-1] + f[-2])
# t = tuple(f)
# print(t)

# ---------------------------------------------------->

# 5.
# count = 0
# t = ((2,5),(4,2),(9,8),(12,10))
# for i in t:
#     if i[0] % 2 == 0 and i[1] % 2 == 0: count += 1
# print(count)

# ------------------------------------------------------>

# 6.
# str_tuple = eval(input("Enter tuple of strings: "))
# length = len(str_tuple[0])
# if len(str_tuple) != 0:
#     for i in str_tuple:
#         if len(i) < length: length = len(i)
#     print(length)
# else: print("No elements in list")

# ----------------------------------------------------->

# L I S T S

# 1.
# Lst*3 only returns a new list with the elements of this list multiplied by 3
# Lst*=3 returns as well as sets the value of the variable "Lst" to the returned value

# ------------------------------------------------------->

# 2.
# l = eval(input("Enter an int list: "))
# rev_l = l[::-1]
# print(rev_l)

# -------------------------------------------------------->

# 3.
# l1 = eval(input("Enter list 1: "))
# l2 = eval(input("Enter list 2: "))
# l3 = l1 + l2
# print(l3)

# ---------------------------------------------------------->

# 4.
# l = eval(input("Enter a list of strings: "))
# new_l = []
# for i in l: new_l.append(i[1:])
# print(new_l)

# ---------------------------------------------------------->

# 5.
# l = []
# for i in range(int(input("Enter number of elements: "))):
#     n = int(input("Enter num between 1-12: "))
#     if n < 1 or n > 12:
#         print("Number out of range")
#         break
#     l.append(n)
# new_l = []
# for i in l:
#     if i > 10: new_l.append(10)
#     else: new_l.append(i)
# print(new_l)

# ------------------------------------------------------->

# 6.
# l = eval(input("enter list"))
# r_l = list(l)[::-1]
# temp = r_l.pop(0)
# r_l = r_l[::-1]
# r_l.insert(0,temp)
# print(r_l)

# ----------------------------------------------------->

# 7.
# l = eval(input("enter list: "))
# m = eval(input("enter list of same size: "))
# n =[]
# if len(l) == len(m):
#     for i in range(len(l)): n.append(l[i] + m[i])
#     print(n)
# else:   print('list not of same size')

# ---------------------------------------------------->

#  F U N C T I O N S

# 1.
# def DollarToRupee_Void(amount : float, conversionFactor: float) -> None:
#     print(amount*conversionFactor)

# def DollarToRupee_NonVoid(amount : float, conversionFactor : float) -> float:
#     return amount*conversionFactor

# DollarToRupee_Void(5,81.2)
# print(DollarToRupee_NonVoid(5,81.2))

# -------------------------------------------------------->

# 2.
# def Volume(l : float = 1.0, b : float = 1.0, h : float = 1.0) -> float:
#     return l*b*h
# print(Volume(4,2))

# --------------------------------------------------------->

# 3.
# def Cube(n: float = 2): print(n**3)
# def isEqual(a: str, b: str) -> bool: return a == b
# Cube(4) #returns 64
# print(isEqual('a','b')) #returns False

# ---------------------------------------------------------->

# 4.
# import random
# def Random(a: int, b: int) -> int: return random.randint(a, b)
# print(Random(1,5), Random(5,10), Random(124,200))

# ----------------------------------------------------------->

# 5.
# def isEqualLen(a: str, b: str) -> bool: return len(a)==len(b)
# print(isEqualLen('124','abc')) #returns True

# ----------------------------------------------------------->

# 6.
# def nthRoot(x: int, n: int = 2) -> float: return x**(1/n)
# print(nthRoot(8,3)) #returns 2.0

# ---------------------------------------------------------->

# 7.
# import random
# def R(n: int) -> int:
#     lowest = int('1' + '0'*(n-1))
#     highest = int('9'*n)
#     return random.randint(lowest, highest)