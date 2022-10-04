class Parent:
  
  name="vivek"
  age=22
  
  def __init__(self):
    pass
    # return "name is {} and age is {}".format({self.name},{self.age})
  
  
  def changeName(self,name):
    self.name=name
  
  def changeAge(self,age):
    self.age=age
    
  def __repr__(s):
    return s.name+"  "+str(s.age)
    
  @classmethod
  def clsChange(cls,name):
    cls.name=name
  
p=Parent()
print(p)
p.clsChange("vivek Jd 122")#this change will be  permamnet for class
print(p)
p.changeName("vivek Jd 18")#this change is temporary till the instance
print(p)
pt=Parent()
print(pt)
