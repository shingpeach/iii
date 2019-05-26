
#2-1
y = -1
sum = 0
for x in range(1, 51, 1):
  sum += ((x**2)*(y**(x-1)))
print(sum)

#2-2
a = int(input("Enter any number:"))
if a > 0:
  for n in range(1, (a+1), 1):
    if (a % n) == 0:
      print(n, end=',')
else:
  print("Error")

#2-3
for i in range(1, 101, 1):
  total = 0
  for j in range(1, i, 1):
    if j < i:
      if i % j == 0:
        total += j
  if i == total:
     print(i, end=',')

#2-4
for x in range(100, 1000):
  a = x//100
  b = x%100//10
  c = x%100%10
  if x == ((a**3) + (b**3) + (c**3)):
    print(x, end=",")


#2-5
n = int(input("Enter any number:"))
for i in range(2, n+1):
  for j in range(2, i):
    if i % j == 0:
      break
  else:
    print(i, end=',')

#另一個解法
i = int(input('Input a number:'))
total = 0
for j in range(1, i, 1):
  if i % j == 0:
    total += j
if total == 1:
  print('{}是質數'.format(i))
else:
  print('{}不是質數'.format(i))

#2-6
for x in range(1, 3000):
  if (3000 / (2**x)) < 5:
    break
print(x)


#2-7
rabbit = 0
while True:
  rabbit += 1
  if rabbit %3 ==1 and rabbit %5 ==3 and rabbit %7 ==2:
        print("{} rabbits".format(rabbit))
        break


#2-8
count = 0
password = '123456'
while count <3:
  psw = str(input("請輸入密碼："))
  if psw == password:
    print("密碼輸入正確，歡迎使用本系統！")
    break
  else:
    count += 1
else:
  print("密碼輸入超過三次！")

#2-9
for n in range(1, 6):
  print(n*'*', end='\n')

width = 5
for n in range(5, 0, -1):
  str1 = n*'*'
  print(str1.rjust(width), end='\n')

width = 15
for n in range(1, 6):
  str1 = n*' * '
  print(str1.center(width), end='\n')

#2-10
print(" ", "|", end=" ")
for n in range(1, 10, 1):
  print(n, end='\t')
print()
print("--------------------------------------")
for i in range(9, 0, -1):
  print(i,"|", end=" ")
  for j in range(1, i+1, 1):
    print("{}".format(i*j), end='\t')
  print()


#2-11
x = 1
while True:
    if 1.05 ** x > (1 + 0.1 * x):
        break
    x += 1
print(x)

#2-12
print(" ", "|", "  銀行  ", "  當鋪  ", "  地下  ", end='\t')
print()
for m in range(1, 13, 1):
    k = 100000
    print("{} | {:.0f}, {:.0f}, {:.0f}".format(m, (1+(0.2/12)*m)*k, (1+0.1*m)*k, (1+0.3*m)*k), end="\t")
    print()
