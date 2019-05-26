#3-1
def power(x, n):
    count = 1
    total = 1
    while True:
        if count <= n:
            total *= x
            count += 1
        else:
            break
    print(total)

def main():
    power(5,3)
main()

#3-2
def my_fun(x, n):
    sum = 0
    for j in range(1, n+1):
        count = 1
        total = 1
        while True:
            if count <= j:
                    total *= x
                    count += 1
            else:
                break

        result = 1
        for i in range(j, 0, -1):
            result *= i

        z = total / result

        sum += z
    print(sum)

#3-3
def is_prime(n):
    if n <2:
        print("Error")
    elif n == 2:
        print("2 is a prime.")
    else:
        for x in range (2, n):
            y = n % x
        if y == 0:
            print("{} is a prime.".format(n))
        else:
            print("{} is not a prime.".format(n))

#3-4
def get_prime (n):
  count = 0
  while count <= n:
    i = 1
    while True:
      i += 1
      for j in range(2, i, 1):
        if i % j == 0:
          break
      else:
        count += 1
      if count == n:
        print(i)
        break

def main():
  print(get_prime(10))
main()

#3-5
def is_mersenne_prime(x):
  count=0
  p=1
  while True:
    p+=1
    i=2**p-1
    for n in range(2, i):
      if i % n == 0:
        break
    else:
      count+=1
    if count==x:
      return i
      break


def main():
  for x in range (1,6):
    print(is_mersenne_prime(x))
main()


#3-6
def factorial(n):
  result = 0
  if n < 1:
    return False
  elif n == 1:
    result = 1
  else:
    result = n*factorial(n-1)
  return result


def main():
  print(factorial(5.5))
main()

#3-7
def factorial(n):
  result = 0
  if n < 1:
    return False
  else:
    result = 2*n + factorial(n-1)
  return result


def main():
  print(factorial(4))
main()


#3-8
def to_binary(x):
  if x < 0:
    print('Error')
  elif x in (0, 1):
    print(x)
  else:
    n = 0
    while True:
      n+=1
      if 2**(n+1) > x:
        print(x//(2**n), end='')
        for i in range(n-1, -1, -1):
          print(x//(2**i)%2, end='')
        break

def to_hexadecimal(x):
  if x < 0:
    print('Error')
  elif x in (0, 1):
    print(x)
  else:
    n = 0
    while True:
      n+=1
      if 16**(n+1) > x:
        if x//(16**n) >= 10:
          if x//(16**n) == 10:
            print('A', end='')
          if x//(16**n) == 11:
            print('B', end='')
          if x//(16**n) == 12:
            print('C', end='')
          if x//(16**n) == 13:
            print('D', end='')
          if x//(16**n) == 14:
            print('E', end='')
          if x//(16**n) == 15:
            print('F', end='')
        else:
          print(x//(16**n), end='')

        for i in range(n-1, -1, -1):
          if x//(16**i)%16 >= 10:
            if x//(16**i)%16 == 10:
              print('A', end='')
            if x//(16**i)%16 == 11:
              print('B', end='')
            if x//(16**i)%16 == 12:
              print('C', end='')
            if x//(16**i)%16 == 13:
              print('D', end='')
            if x//(16**i)%16 == 14:
              print('E', end='')
            if x//(16**i)%16 == 15:
              print('F', end='')
          else:
            print(x//(16**i)%16, end='')
        break

def main():
  to_binary(427)
  print()
  to_hexadecimal(427)
main()

#3-9
def to_binary(x):
  if x >= 2:
    to_binary(x//2)
  print(x%2, end='')

def to_hexadecimal(x):
  if x >= 16:
    to_hexadecimal(x//16)
  if x%16 >= 10:
    if x%16 == 10:
      print('A', end='')
    if x%16 == 11:
      print('B', end='')
    if x%16 == 12:
      print('C', end='')
    if x%16 == 13:
      print('D', end='')
    if x%16 == 14:
      print('E', end='')
    if x%16 == 15:
      print('F', end='')
    print('A', end='')
  else:
    print(x%16, end='')

def main():
  to_binary(357)
  to_hexadecimal(357)
main()


