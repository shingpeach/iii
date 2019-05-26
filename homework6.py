
# 6-1
class Level00:
    def __init__(self, no, level, name, gender, hiredate, tel, address, salary, extra_hours):
        self.no = no
        self.level = level
        self.name = name
        self.gender = gender
        self.hiredate = hiredate
        self.tel = tel
        self.address = address
        self.salary = salary
        self.extra_hours = extra_hours

    def __str__(self):
        return ('no={0}, level={1}, name={2}, gender={3}, hiredate={4}, tel={5}, address={6}, salary={7}, extra_hours={8}'\
                .format(self.no, self.level, self.name, self.gender, self.hiredate, self.tel, self.address, self.salary, self.extra_hours))


class Level01(Level00):
    def __init__(self, no, level, name, gender, hiredate, tel, address, salary, extra_hours, total_salary=salary):
        super(Level01, self).__init__(no, level, name, gender, hiredate, tel, address, salary, extra_hours)
        self.total_salary = total_salary

    def total_salary(self):
        print('本月總薪資為${}'.format(self.salary + (self.salary / 240 * self.extra_hours)))


class Level10(Level01):
    def __init__(self, no, level, name, gender, hiredate, tel, address, salary, extra_hours, lunch=1800, traffic=2000, managebonus=5000):
        super(Level10, self).__init__(no, level, name, gender, hiredate, tel, address, salary, extra_hours)
        self.lunch = lunch
        self.traffic = traffic
        self.managebonus = managebonus

    def total_salary(self):
        print('本月總薪資為${}'.format(self.salary + (self.salary / 240 * self.extra_hours) + self.lunch + self.traffic + self.managebonus))

    def __str__(self):
        return (super(Level10, self).__str__() + ', lunchbonus={0}, trafficbonus={1}, managebonus={2}'.format(self.lunch, self.traffic, self.managebonus))


class Level20(Level01):
    def __init__(self, no, level, name, gender, hiredate, tel, address, salary, extra_hours, lunch=1800, managebonus=3000):
        super(Level20, self).__init__(no, level, name, gender, hiredate, tel, address, salary, extra_hours)
        self.lunch = lunch
        self.managebonus = managebonus

    def total_salary(self):
        print('本月總薪資為${}'.format(self.salary + (self.salary / 240 * self.extra_hours) + self.lunch + + self.managebonus))

    def __str__(self):
        return (super(Level20, self).__str__() + ', lunchbonus={0}, managebonus={1}'.format(self.lunch, self.managebonus))


def main():
    emp1 = Level01('001', '01', 'A', 'F', '2009/05/22', '0911111111', 'aaa', 58000, 0)
    emp2 = Level10('002', '10', 'B', 'M', '2010/04/08', '0922222222', 'bbb', 69000, 15)
    emp3 = Level20('003', '20', 'C', 'F', '2019/06/29', '0933333333', 'ccc', 120000, 0)
    emp4 = Level01('004', '01', 'D', 'M', '2012/03/22', '0944444444', 'ddd', 28000, 30)
    emp5 = Level01('005', '01', 'E', 'F', '2018/09/09', '0955555555', 'eee', 32000, 8)
    emp6 = Level10('006', '10', 'F', 'M', '2016/12/25', '0966666666', 'fff', 43000, 0)

    print(emp1)
    print(emp2)
    print(emp3)
    print(emp4)
    print(emp5)
    print(emp6)


main()
'''

#6-2
class StackEmptyError(Exception):
    pass

class Stack:
  def __init__(self, list1):
      self.list1 = list1

  def push(self, x):
      s = self.list1
      s.append(x)
      print(s)

  def pop(self):
      try:
          s = self.list1
          if len(s) == 0:
              raise StackEmptyError
          else:
              s.pop()
              print(s)
      except StackEmptyError:
          print('Stack is empty!')

def main():
    list1=[]
    s1 = Stack(list1)
    s1.pop()

main()

    
#6-3
'''


