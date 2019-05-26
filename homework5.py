class human:
  def __init__(self,name,sex,arrivaldate,phone,address):
    self.name = name
    self.sex = sex
    self.arrivaldate = arrivaldate
    self.phone = phone
    self.address = address
  def __str__(self):
    return('name : {}\nsex : {}\narrival date : {}\nphone : {}\naddress : {}'.format(self.name,self.sex,self.arrivaldate,self.phone,self.address))

class basic(human):
  def __init__(self,name,sex,arrivaldate,phone,address,basicsalary,overhour,salary=0):
    super(basic,self).__init__(name,sex,arrivaldate,phone,address)
    self.basicsalary = basicsalary
    self.overhour=overhour
    self.salary=salary= int(self.basicsalary) * (1 + (int(self.overhour)*1.5)/240)

  def __str__(self):
    return super(basic,self).__str__()\
    +"\nbasic salary : {}\nover hours : {}\nsalary for this month :{} ".format(self.basicsalary,self.overhour,self.salary)


class manager2(basic):
  def __init__(self,name,sex,arrivaldate,phone,address,basicsalary,overhour,managerbones= 3000,launchbones= 1800,trafficbones= 2000):
    super(manager2,self).__init__(name,sex,arrivaldate,phone,address,basicsalary,overhour)
    self.managerbones = managerbones
    self.launchbones = launchbones
    self.trafficbones = trafficbones
    self.salary=salary= self.basicsalary * (1 + (self.overhour*1.5)/240) +self.managerbones+self.launchbones+self.trafficbones
  def __str__(self):
    return super(manager2,self).__str__()\
    +"\nmanager bones : {}\nlaunch bones : {}\ntraffic bones : {}".format(self.managerbones,self.launchbones,self.trafficbones)

class manager1(manager2):
  def __init__(self,name,sex,arrivaldate,phone,address,basicsalary,overhour,managerbones= 5000,launchbones= 1800,trafficbones= 2000):
    super(manager1,self).__init__(name,sex,arrivaldate,phone,address,basicsalary,overhour,managerbones,launchbones,trafficbones)

def main():
    emp1 = basic('A', 'F', '2009/05/22', '0911111111', 'aaa', 58000, 0)
    print(emp1)

