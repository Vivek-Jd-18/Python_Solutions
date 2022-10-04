code = 'a=5\nb=2\nc=a+b\nprint(c)'
fire=compile(code,"sum",'exec')
exec(fire)