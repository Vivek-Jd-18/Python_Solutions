class Demo:
  name="Azpilicueta"
  age=39
  
  #The __repr__() function returns a string containing a printable representation of an object.
  def __repr__(_):
    return f"player {_.name} aged {_.age}"
    

d=Demo()
print(d)