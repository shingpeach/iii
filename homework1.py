
#1
month = eval(input("input month in number:"))
if 1 <= month <= 3:
    print("春")
elif 4 <= month <= 6:
    print("夏")
elif 7 <= month <= 9:
    print("秋")
elif 10 <= month <= 12:
    print("冬")
else :
    print("輸入錯誤")

#2
hour = eval(input("Enter working hours:"))
if 0 <= hour <= 60:
  print("Total is {}" .format(hour * 120))
elif 60 < hour <= 80:
  print("Total is {}" .format((hour-60) * 120 * 1.25 + 60 * 120))
elif 80 < hour:
  print("Total is {}" .format((hour-80) * 120 * 1.5 + 20 * 120 * 1.25 + 60 * 120))
else:
  print("Error")

#3
a = input("Choose the type of electricity, 'Family' or 'Industry': ")
if a == "Industry" :
  x = eval(input("Enter your electricity consumption:"))
  if 0 <= x :
    print("The total electricity fee is {}" .format(x * 0.45))
  else:
    print("Error")
elif a == "Family" :
  x = eval(input("Enter your electricity consumption:"))
  if 0 <= x <= 240 :
    print("The total electricity fee is {}" .format(x * 0.15))
  elif 240 < x <= 540 :
    print("The total electricity fee is {}" .format(240 * 0.15 + (540 - x) * 0.25))
  elif 540 < x  :
    print("The total electricity fee is {}" .format(240 * 0.15 + 300 * 0.25 + (x - 540) * 0.45))
else:
  print("Error")

#4
year = eval(input("Enter any year: "))
if year % 4 == 0:
  if year % 100 != 0:
    print("{}是閏年" .format(year))
elif year % 400 == 0:
  if year % 4000 != 0:
    print("{}是閏年" .format(year))
else:
  print("{}不是閏年" .format(year))

#5
(x, y) = eval(input("Enter 'the amout you should pay, the amount actually paid' : "))
if y < x :
  print("金額不足")
if y == x :
  print("不必找錢")
if y > x :
  print("找您{0}張500元,{1}張100元,{2}個50元,{3}個10元,{4}個5元,{5}個1元"
  .format((y-x)//500, (y-x)%500//100, (y-x)%500%100//50,
  (y-x)%500%100%50//10, (y-x)%500%100%50%10//5, (y-x)%500%100%50%10%5))


#6
(a, b, c) = eval(input("Enter three numbers for 'a, b, c' : "))
if (b**2-4*a*c) < 0:
    print('沒有實根')
elif (b**2-4*a*c) == 0:
    import math
    x = ((b*(-1)+ math.sqrt(b ** 2 - 4 * a * c))/2*a)
    print(x)
else:
    import math
    x1 = ((b*(-1)+ math.sqrt(b ** 2 - 4 * a * c))/2*a)
    x2 = ((b * (-1) - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
    print(x1, x2, end=',')


