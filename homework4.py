# 4-1
def mymax(*num):
    for i in num:
        for j in num:
            if i < j:
                break
        else:
            print(i)


def mymin(*num):
    for i in num:
        for j in num:
            if i > j:
                break
        else:
            print(i)


def main():
    mymax(1, 2, 3)
    mymin(1, 2, 3)


main()


# 4-2
def myavg(num):
    list1 = []
    for i in range(len(num)):
        for j in range(len(num[i])):
            list1.append(num[i][j])
    sum = 0
    for k in list1:
        sum += k
    print(sum / len(list1))


def mymax(num):
    list1 = []
    for i in range(len(num)):
        for j in range(len(num[i])):
            list1.append(num[i][j])
    for k in list1:
        for l in list1:
            if k < l:
                break
        else:
            print(k)


def mymin(num):
    list1 = []
    for i in range(len(num)):
        for j in range(len(num[i])):
            list1.append(num[i][j])
    for k in list1:
        for l in list1:
            if k > l:
                break
        else:
            print(k)


def myavg_div(num):
    for i in range(len(num)):
        list1 = (num[i])
        sum = 0
        for k in list1:
            sum += k
        print(sum / len(list1))


def main():
    num = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    myavg(num)
    mymax(num)
    mymin(num)
    myavg_div(num)


main()

# 4-3
name = ['Jean', 'Tom', 'Tina']
product = ['A', 'B', 'C', 'D', 'E']
price = [12, 16, 10, 14, 15]
sales = [[33, 32, 56, 45, 33], [77, 33, 68, 45, 23], [43, 55, 43, 67, 65]]
total = []

for i in range(len(sales)):
    total.append([])
    for j in range(len(sales[i])):
        total[i].append(sales[i][j] * price[j])

print('{0}銷售總金額:${1}\n{2}銷售總金額:${3}\n{4}銷售總金額:${5}'.format(name[0], sum(total[0]), name[1], sum(total[1]), name[2],
                                                           sum(total[2])))

maxname = name[0]
maxsum = sum(total[0])
for x in range(len(total)):
    if maxsum < sum(total[x]):
        maxsum = sum(total[x])
        maxname = name[x]
print('業績最好者為{}, 銷售總金額為${}'.format(maxname, maxsum))

pro_sum = []
for k in range(len(sales[0])):
    pro_sum.append([])
    for l in range(len(sales)):
        pro_sum[k].append(sales[l][k] * price[k])

print(product[0], sum(pro_sum[0]), product[1], sum(pro_sum[1]), product[2], sum(pro_sum[2]), product[3],
      sum(pro_sum[3]), product[4], sum(pro_sum[4]))

max_pro = product[0]
max_pro_sum = sum(pro_sum[0])
for y in range(len(pro_sum)):
    if max_pro_sum < sum(pro_sum[y]):
        max_pro_sum = sum(pro_sum[y])
        max_pro = product[y]
print(max_pro, max_pro_sum)

#4-4


